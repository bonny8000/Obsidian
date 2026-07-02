[CmdletBinding()]
param(
    [string]$PackagePath,
    [switch]$PackageOnly
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$packagesRoot = [System.IO.Path]::GetFullPath((Join-Path $repoRoot 'wiki\drafts\packages'))

function Resolve-PackagePath {
    param([Parameter(Mandatory = $true)][string]$Path)

    $candidate = if ([System.IO.Path]::IsPathRooted($Path)) {
        [System.IO.Path]::GetFullPath($Path)
    }
    else {
        [System.IO.Path]::GetFullPath((Join-Path $repoRoot $Path))
    }

    if (Test-Path -LiteralPath $candidate -PathType Leaf) {
        $candidate = Split-Path -Parent $candidate
    }

    $packagePrefix = $packagesRoot.TrimEnd('\') + '\'
    if (-not $candidate.StartsWith($packagePrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Package must stay inside $packagesRoot. Received: $candidate"
    }

    return $candidate
}

function Test-TargetPath {
    param([Parameter(Mandatory = $true)][string]$RelativePath)

    if ([System.IO.Path]::IsPathRooted($RelativePath)) {
        throw "Absolute target path is not allowed: $RelativePath"
    }

    $normalized = $RelativePath.Replace('/', '\').TrimStart('\')
    if ($normalized -match '(^|\\)\.\.(\\|$)') {
        throw "Parent traversal is not allowed: $RelativePath"
    }

    if ($normalized -notmatch '^wiki\\(sources|concepts)\\.+\.md$') {
        throw "Target is outside allowed draft roots: $RelativePath"
    }
}

function Test-MarkdownContent {
    param(
        [Parameter(Mandatory = $true)][string]$RelativePath,
        [Parameter(Mandatory = $true)][string]$Content
    )

    if ([string]::IsNullOrWhiteSpace($Content)) {
        throw "Empty content: $RelativePath"
    }

    if ($Content -notmatch '^---\r?\n') {
        throw "Missing YAML frontmatter: $RelativePath"
    }

    if ($Content -notmatch '(?m)^#\s+\S') {
        throw "Missing H1: $RelativePath"
    }

    if ($Content -match '\{\{|TODO|TBD|\uFFFD') {
        throw "Placeholder or replacement character found: $RelativePath"
    }

    if ($RelativePath.Replace('\', '/') -like 'wiki/sources/*') {
        $required = @(
            'Citation', 'Summary', 'Key Claims', 'Useful Examples', 'Constraints / Caveats',
            'Design Implications', 'Tensions', 'Open Questions', 'Concepts Linked',
            'LLM Use', 'Reliability Notes', 'Backfill Status'
        )

        foreach ($heading in $required) {
            if ($Content -notmatch "(?m)^## $([regex]::Escape($heading))\s*$") {
                throw "Missing source section '$heading': $RelativePath"
            }
        }
    }
}

if ($PackagePath) {
    $resolvedPackage = Resolve-PackagePath -Path $PackagePath
    $manifestPath = Join-Path $resolvedPackage 'manifest.json'

    if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
        throw "Manifest missing: $manifestPath"
    }

    $manifest = Get-Content -Raw -LiteralPath $manifestPath -Encoding UTF8 | ConvertFrom-Json
    if ($manifest.schema_version -ne 1) {
        throw "Unsupported manifest schema: $($manifest.schema_version)"
    }

    if ($manifest.status -notin @('review', 'applied')) {
        throw "Invalid manifest status: $($manifest.status)"
    }

    $operations = @($manifest.operations)
    if ($operations.Count -eq 0) {
        throw 'Manifest contains no operations.'
    }

    $seen = @{}
    foreach ($operation in $operations) {
        $relativePath = [string]$operation.path
        Test-TargetPath -RelativePath $relativePath

        $pathKey = $relativePath.ToLowerInvariant()
        if ($seen.ContainsKey($pathKey)) {
            throw "Duplicate operation target: $relativePath"
        }

        $seen[$pathKey] = $true
        if ([string]$operation.action -notin @('create', 'replace')) {
            throw "Invalid action: $($operation.action)"
        }

        Test-MarkdownContent -RelativePath $relativePath -Content ([string]$operation.content)
    }

    Write-Host "Package valid: $resolvedPackage" -ForegroundColor Green
}

if ($PackageOnly) {
    return
}

Write-Host 'Validating Canvas files...' -ForegroundColor Cyan
$canvasFiles = Get-ChildItem -LiteralPath (Join-Path $repoRoot 'wiki\canvases') -Filter '*.canvas' -File -ErrorAction SilentlyContinue
foreach ($canvasFile in $canvasFiles) {
    $canvas = Get-Content -Raw -LiteralPath $canvasFile.FullName -Encoding UTF8 | ConvertFrom-Json
    $nodeIds = @($canvas.nodes | ForEach-Object { $_.id })
    $edgeIds = @($canvas.edges | ForEach-Object { $_.id })
    $allIds = @($nodeIds) + @($edgeIds)

    if (($allIds | Select-Object -Unique).Count -ne $allIds.Count) {
        throw "Duplicate Canvas IDs: $($canvasFile.Name)"
    }

    foreach ($id in $allIds) {
        if ([string]$id -notmatch '^[0-9a-f]{16}$') {
            throw "Invalid Canvas ID '$id': $($canvasFile.Name)"
        }
    }

    foreach ($edge in @($canvas.edges)) {
        if ($edge.fromNode -notin $nodeIds -or $edge.toNode -notin $nodeIds) {
            throw "Dangling Canvas edge: $($canvasFile.Name) / $($edge.id)"
        }
    }

    foreach ($node in @($canvas.nodes)) {
        if ($node.type -eq 'file') {
            $fileTarget = [System.IO.Path]::GetFullPath((Join-Path $repoRoot ([string]$node.file)))
            if (-not (Test-Path -LiteralPath $fileTarget)) {
                throw "Missing Canvas file node: $($node.file)"
            }
        }
    }

    Write-Host "  $($canvasFile.Name): valid"
}

$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCommand) {
    throw 'Python is required for scripts/lint.py.'
}

Write-Host 'Running vault lint...' -ForegroundColor Cyan
& $pythonCommand.Source (Join-Path $repoRoot 'scripts\lint.py')
if ($LASTEXITCODE -ne 0) {
    throw "Vault lint failed with exit code $LASTEXITCODE"
}

Write-Host 'Running git diff --check...' -ForegroundColor Cyan
& git -C $repoRoot diff --check
if ($LASTEXITCODE -ne 0) {
    throw "git diff --check failed with exit code $LASTEXITCODE"
}

Write-Host 'Ingest validation passed.' -ForegroundColor Green
