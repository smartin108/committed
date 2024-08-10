$repoRootDir = "C:\Users\Z40\Documents\git"

Get-ChildItem -Recurse -Filter ".git" -Directory -ErrorAction SilentlyContinue -Path $repoRootDir | ForEach-Object {
    $repoDir = $_.FullName.Substring(0, $_.FullName.Length - 4) # Remove ".git" from the end of the path
    Write-Output "`nProcessing repository at: $repoDir"
    
    try {
        Set-Location $repoDir
        
        # Confirm current directory is the repository
        Write-Output "Current directory: $(Get-Location)"
        
        # Check if this is actually a git repository
        if (-not (Test-Path "$repoDir\.git")) {
            Write-Output "Not a git repository: $repoDir"
            return
        }

        git add .

        # Check if there are any staged changes
        if (-not (git diff --cached --quiet)) {
            Write-Output "Changes detected, committing..."
            git commit -m "automatic commit"
            git push
        } else {
            Write-Output "No changes detected, skipping commit."
        }
    } catch {
        Write-Output "An error occurred while processing $repoDir: $_"
    }
}

# Return to the original directory
Set-Location $repoRootDir
