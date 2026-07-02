[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
param(
    [string]$PackagePath,
    [switch]$AllowReplace,
    [switch]$SkipValidation
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$packagesRoot = [System.IO.Path]::GetFullPath((Join-Path $repoRoot 'wiki\drafts\packages'))

function Get-ReviewPackage {
    param([string]$RequestedPath)

    if ($RequestedPath) {
        $candidate = if ([System.IO.Path]::IsPathRooted($RequestedPath)) {
            [System.IO.Path]::GetFullPath($RequestedPath)
        }
        else {
            [System.IO.Path]::GetFullPath((Join-Path $repoRoot $RequestedPath))
        }
        if (Test-Path -LiteralPath $candidate -PathType Leaf) {
            if ([System.IO.Path]::GetFileName($candidate) -ne 'manifest.json') {
                throw "Package file must be manifest.json: $candidate"
            }
            return Split-Path -Parent $candidate
        }
        return $candidate
    }

    if (-not (Test-Path -LiteralPath $packagesRoot -PathType Container)) {
        throw 'No draft packages exist. Run draft-with-ollama.ps1 first.'
    }

    $latest = Get-ChildItem -LiteralPath $packagesRoot -Directory | Sort-Object LastWriteTime -Descending | Where-Object {
        $manifestFile = Join-Path $_.FullName 'manifest.json'
        if (-not (Test-Path -LiteralPath $manifestFile)) { return $false }
        try {
            $candidateManifest = Get-Content -Raw -LiteralPath $manifestFile -Encoding UTF8 | ConvertFrom-Json
            return $candidateManifest.status -eq 'review'
        }
        catch { return $false }
    } | Select-Object -First 1

    if (-not $latest) {
        throw 'No draft package with status=review was found.'
    }
    return $latest.FullName
}

function Resolve-TargetPath {
    param([Parameter(Mandatory = $true)][string]$RelativePath)

    if ([System.IO.Path]::IsPathRooted($RelativePath)) {
        throw "Absolute target path is not allowed: $RelativePath"
    }
    $normalized = $RelativePath.Replace('/', '\').TrimStart('\')
    if ($normalized -match '(^|\\)\.\.(\\|$)') {
        throw "Parent traversal is not allowed: $RelativePath"
    }
    if ($normalized -notmatch '^wiki\\(sources|concepts)\\.+\.md$') {
        throw "Apply targets are restricted to wiki/sources or wiki/concepts Markdown files: $RelativePath"
    }
    $fullPath = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $normalized))
    $wikiRoot = [System.IO.Path]::GetFullPath((Join-Path $repoRoot 'wiki'))
    if (-not $fullPath.StartsWith($wikiRoot.TrimEnd('\') + '\', [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Target escaped the wiki root: $RelativePath"
    }
    return $fullPath
}

$resolvedPackage = Get-ReviewPackage -RequestedPath $PackagePath
$resolvedPackage = [System.IO.Path]::GetFullPath($resolvedPackage)
if (-not $resolvedPackage.StartsWith($packagesRoot.TrimEnd('\') + '\', [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Package must stay inside $packagesRoot. Received: $resolvedPackage"
}

$manifestPath = Join-Path $resolvedPackage 'manifest.json'
if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
    throw "Package manifest not found: $manifestPath"
}

if (-not $SkipValidation) {
    & (Join-Path $PSScriptRoot 'validate-ingest.ps1') -PackagePath $resolvedPackage -PackageOnly
}

$manifest = Get-Content -Raw -LiteralPath $manifestPath -Encoding UTF8 | ConvertFrom-Json
if ($manifest.status -ne 'review') {
    throw "Only packages with status=review can be applied. Current status: $($manifest.status)"
}

$operations = @($manifest.operations)
if ($operations.Count -eq 0) { throw 'Package contains no operations.' }

$resolvedOperations = foreach ($operation in $operations) {
    $action = [string]$operation.action
    if ($action -notin @('create', 'replace')) { throw "Unsupported action: $action" }
    if ($action -eq 'replace' -and -not $AllowReplace) {
        throw "Package wants to replace $($operation.path). Review it, then rerun with -AllowReplace."
    }
    $target = Resolve-TargetPath -RelativePath ([string]$operation.path)
    $exists = Test-Path -LiteralPath $target -PathType Leaf
    if ($action -eq 'create' -and $exists) {
        throw "Create target already exists: $target"
    }
    if ($action -eq 'replace' -and -not $exists) {
        throw "Replace target does not exist: $target"
    }
    [pscustomobject]@{
        Action  = $action
        RelativePath = [string]$operation.path
        Target  = $target
        Content = ([string]$operation.content).Trim() + "`n"
        Existed = $exists
    }
}

Write-Host "Package: $($manifest.package_id)" -ForegroundColor Cyan
$resolvedOperations | Format-Table Action, RelativePath -AutoSize

if (-not $PSCmdlet.ShouldProcess("$($resolvedOperations.Count) wiki file(s)", "Apply reviewed package $($manifest.package_id)")) {
    return
}

$backupRoot = Join-Path $resolvedPackage ('backup-' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
[System.IO.Directory]::CreateDirectory($backupRoot) | Out-Null
$applied = New-Object System.Collections.Generic.List[object]

try {
    foreach ($operation in $resolvedOperations) {
        $parent = Split-Path -Parent $operation.Target
        [System.IO.Directory]::CreateDirectory($parent) | Out-Null
        $backupPath = $null
        if ($operation.Existed) {
            $backupName = $operation.RelativePath.Replace('/', '__').Replace('\', '__')
            $backupPath = Join-Path $backupRoot $backupName
            Copy-Item -LiteralPath $operation.Target -Destination $backupPath
        }
        [System.IO.File]::WriteAllText($operation.Target, $operation.Content, $script:Utf8NoBom)
        $applied.Add([pscustomobject]@{ Target = $operation.Target; Existed = $operation.Existed; Backup = $backupPath })
    }

    if (-not $SkipValidation) {
        & (Join-Path $PSScriptRoot 'validate-ingest.ps1')
    }

    $manifest | Add-Member -NotePropertyName applied_at -NotePropertyValue ((Get-Date).ToString('o')) -Force
    $manifest.status = 'applied'
    [System.IO.File]::WriteAllText($manifestPath, ($manifest | ConvertTo-Json -Depth 20), $script:Utf8NoBom)
}
catch {
    foreach ($entry in @($applied) | Sort-Object -Property Target -Descending) {
        if ($entry.Existed -and $entry.Backup) {
            Copy-Item -LiteralPath $entry.Backup -Destination $entry.Target -Force
        }
        elseif (Test-Path -LiteralPath $entry.Target) {
            Remove-Item -LiteralPath $entry.Target -Force
        }
    }
    throw "Apply failed and written files were rolled back. $($_.Exception.Message)"
}

Write-Host 'Draft applied and validated.' -ForegroundColor Green
Write-Host "Backup directory: $backupRoot"
