[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RawPath,

    [string]$Model = 'qwen3:4b',

    [ValidateRange(2000, 50000)]
    [int]$MaxSourceChars = 12000,

    [string]$ApiBase = 'http://localhost:11434'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$rawRoot = [System.IO.Path]::GetFullPath((Join-Path $repoRoot 'raw'))
$draftRoot = Join-Path $repoRoot 'wiki\drafts\packages'

function Resolve-InsideRoot {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Root
    )

    $candidate = if ([System.IO.Path]::IsPathRooted($Path)) {
        [System.IO.Path]::GetFullPath($Path)
    }
    else {
        [System.IO.Path]::GetFullPath((Join-Path $repoRoot $Path))
    }

    $prefix = $Root.TrimEnd('\') + '\'
    if ($candidate -ne $Root -and -not $candidate.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Path must stay inside $Root. Received: $candidate"
    }
    return $candidate
}

function Resolve-WikiTarget {
    param([Parameter(Mandatory = $true)][string]$RelativePath)

    if ([System.IO.Path]::IsPathRooted($RelativePath)) {
        throw "Draft target must be relative: $RelativePath"
    }
    $normalized = $RelativePath.Replace('/', '\').TrimStart('\')
    if ($normalized -match '(^|\\)\.\.(\\|$)') {
        throw "Parent traversal is not allowed: $RelativePath"
    }
    if ($normalized -notmatch '^wiki\\(sources|concepts)\\.+\.md$') {
        throw "Draft targets are restricted to wiki/sources or wiki/concepts Markdown files: $RelativePath"
    }
    return $normalized.Replace('\', '/')
}

$rawFullPath = Resolve-InsideRoot -Path $RawPath -Root $rawRoot
if (-not (Test-Path -LiteralPath $rawFullPath -PathType Leaf)) {
    throw "Raw source not found: $rawFullPath"
}

$extension = [System.IO.Path]::GetExtension($rawFullPath).ToLowerInvariant()
if ($extension -notin @('.md', '.txt')) {
    throw 'Local drafting accepts Markdown or text raw cards. For a PDF, create or select its raw/web evidence card first.'
}

try {
    $tags = Invoke-RestMethod -Method Get -Uri "$ApiBase/api/tags" -TimeoutSec 10
}
catch {
    throw "Ollama is installed but its API is not reachable at $ApiBase. Start Ollama from the Windows Start menu and retry. $($_.Exception.Message)"
}

$installedModels = @($tags.models | ForEach-Object { $_.name })
if ($Model -notin $installedModels) {
    $installedText = if ($installedModels.Count -eq 0) { 'none' } else { $installedModels -join ', ' }
    throw "Model '$Model' is not installed. Installed models: $installedText. Install it explicitly with: ollama pull $Model"
}

$sourceText = [System.IO.File]::ReadAllText($rawFullPath, [System.Text.Encoding]::UTF8)
$wasTruncated = $false
if ($sourceText.Length -gt $MaxSourceChars) {
    $sourceText = $sourceText.Substring(0, $MaxSourceChars)
    $wasTruncated = $true
}

$relativeRawPath = $rawFullPath.Substring($repoRoot.Length).TrimStart('\').Replace('\', '/')
$schema = @{
    type                 = 'object'
    additionalProperties = $false
    properties           = @{
        source = @{
            type                 = 'object'
            additionalProperties = $false
            properties           = @{
                path    = @{ type = 'string' }
                content = @{ type = 'string' }
            }
            required = @('path', 'content')
        }
        concepts = @{
            type     = 'array'
            maxItems = 1
            items    = @{
                type                 = 'object'
                additionalProperties = $false
                properties           = @{
                    path    = @{ type = 'string' }
                    content = @{ type = 'string' }
                }
                required = @('path', 'content')
            }
        }
        map_suggestions = @{ type = 'array'; items = @{ type = 'string' }; maxItems = 5 }
        review_notes    = @{ type = 'array'; items = @{ type = 'string' }; maxItems = 10 }
    }
    required = @('source', 'concepts', 'map_suggestions', 'review_notes')
}

$systemPrompt = @'
You draft reviewable Obsidian wiki changes. Preserve provenance and uncertainty. Never invent citations, URLs, authors, dates, metrics, or completed verification. Return exactly one source page and at most one durable concept page. Do not propose raw-file edits, deletion, scripts, configuration, maps, indexes, or logs. New source pages must contain YAML frontmatter and these headings: Citation, Summary, Key Claims, Useful Examples, Constraints / Caveats, Design Implications, Tensions, Open Questions, Concepts Linked, LLM Use, Reliability Notes, Backfill Status. Use lowercase kebab-case paths. Keep claims concise and distinguish source claims from interpretation.
'@

$userPrompt = @"
Create a draft ingest package from this preserved raw card.

Raw path: $relativeRawPath
Capture truncated for local context: $wasTruncated
Today: $(Get-Date -Format 'yyyy-MM-dd')

Allowed output paths:
- wiki/sources/<lowercase-kebab-case>.md
- optionally one wiki/concepts/<cluster>/<lowercase-kebab-case>.md

The output is only a draft for human review. Existing files require an explicit replace approval later.

RAW CARD START
$sourceText
RAW CARD END
"@

$request = @{
    model    = $Model
    stream   = $false
    think    = $false
    format   = $schema
    options  = @{ temperature = 0; num_ctx = 8192 }
    messages = @(
        @{ role = 'system'; content = $systemPrompt }
        @{ role = 'user'; content = $userPrompt }
    )
}

$requestJson = $request | ConvertTo-Json -Depth 30 -Compress
try {
    $response = Invoke-RestMethod -Method Post -Uri "$ApiBase/api/chat" -ContentType 'application/json; charset=utf-8' -Body $requestJson -TimeoutSec 1800
}
catch {
    throw "Ollama generation failed. $($_.Exception.Message)"
}

try {
    $draft = $response.message.content | ConvertFrom-Json
}
catch {
    throw "Ollama returned invalid structured JSON. $($_.Exception.Message)"
}

$operations = New-Object System.Collections.Generic.List[object]
$items = @($draft.source) + @($draft.concepts)
foreach ($item in $items) {
    if ($null -eq $item) { continue }
    $relativeTarget = Resolve-WikiTarget -RelativePath ([string]$item.path)
    $targetFullPath = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $relativeTarget.Replace('/', '\')))
    $action = if (Test-Path -LiteralPath $targetFullPath) { 'replace' } else { 'create' }
    $content = ([string]$item.content).Trim() + "`n"
    if ([string]::IsNullOrWhiteSpace($content)) {
        throw "Ollama produced empty content for $relativeTarget"
    }
    $operations.Add([pscustomobject]@{
            action  = $action
            path    = $relativeTarget
            content = $content
        })
}

if ($operations.Count -eq 0) {
    throw 'Ollama produced no file operations.'
}

$baseSlug = [System.IO.Path]::GetFileNameWithoutExtension($rawFullPath).ToLowerInvariant()
$baseSlug = ($baseSlug -replace '[^a-z0-9-]+', '-').Trim('-')
if ([string]::IsNullOrWhiteSpace($baseSlug)) { $baseSlug = 'ingest' }
$packageId = '{0}-{1}-{2}' -f (Get-Date -Format 'yyyyMMdd-HHmmss'), $baseSlug, (Get-Random -Minimum 1000 -Maximum 9999)
$packagePath = Join-Path $draftRoot $packageId
[System.IO.Directory]::CreateDirectory($packagePath) | Out-Null

$manifest = [ordered]@{
    schema_version = 1
    package_id     = $packageId
    status         = 'review'
    created_at     = (Get-Date).ToString('o')
    model          = $Model
    raw_path       = $relativeRawPath
    source_truncated = $wasTruncated
    operations     = @($operations)
    map_suggestions = @($draft.map_suggestions)
    review_notes    = @($draft.review_notes)
}

$manifestPath = Join-Path $packagePath 'manifest.json'
[System.IO.File]::WriteAllText($manifestPath, ($manifest | ConvertTo-Json -Depth 20), $script:Utf8NoBom)

$review = New-Object System.Text.StringBuilder
[void]$review.AppendLine('---')
[void]$review.AppendLine('type: ingest-draft')
[void]$review.AppendLine('status: review')
[void]$review.AppendLine("created: $(Get-Date -Format 'yyyy-MM-dd')")
[void]$review.AppendLine("model: $Model")
[void]$review.AppendLine("raw_path: $relativeRawPath")
[void]$review.AppendLine('---')
[void]$review.AppendLine()
[void]$review.AppendLine("# Review Draft: $packageId")
[void]$review.AppendLine()
[void]$review.AppendLine('> [!warning] Draft only')
[void]$review.AppendLine('> Review every claim and path. Nothing in this package has been applied to the durable wiki.')
foreach ($operation in $operations) {
    [void]$review.AppendLine()
    [void]$review.AppendLine(('## {0}: `{1}`' -f $operation.action, $operation.path))
    [void]$review.AppendLine()
    [void]$review.AppendLine('````markdown')
    [void]$review.AppendLine($operation.content.TrimEnd())
    [void]$review.AppendLine('````')
}
[void]$review.AppendLine()
[void]$review.AppendLine('## Map Suggestions (manual only)')
foreach ($suggestion in @($draft.map_suggestions)) { [void]$review.AppendLine("- $suggestion") }
[void]$review.AppendLine()
[void]$review.AppendLine('## Review Notes')
foreach ($note in @($draft.review_notes)) { [void]$review.AppendLine("- $note") }

$reviewPath = Join-Path $packagePath 'review.md'
[System.IO.File]::WriteAllText($reviewPath, $review.ToString(), $script:Utf8NoBom)

& (Join-Path $PSScriptRoot 'validate-ingest.ps1') -PackagePath $packagePath -PackageOnly

Write-Host "Draft package created: $packagePath" -ForegroundColor Green
Write-Host "Review: $reviewPath"
Write-Host "After review, run: .\scripts\apply-latest-draft.ps1 -PackagePath '$packagePath' -Confirm"
