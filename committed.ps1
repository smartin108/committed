$repoRootDir = "C:\Users\Z40\Documents\git"

Get-ChildItem -Recurse -Filter ".git" -Directory -ErrorAction SilentlyContinue -Path $repoRootDir | ForEach-Object {
    $repoDir = $_.FullName.Substring(0, $_.FullName.Length - 4) # Remove ".git" from the end of the path
    Write-Host "Processing repository at: $repoDir"
    
    Set-Location $repoDir

    git add .

    # Check if there are any staged changes
    if (-not (git diff --cached --quiet)) {
        Write-Host "Changes detected, committing..."
        git commit -m "automatic commit"
        git push
    } else {
        Write-Host "No changes detected, skipping commit."
    }
}

# Return to the original directory
Set-Location $repoRootDir
