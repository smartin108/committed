$repoRootDir = "C:\Users\Z40\Documents\git"

Get-ChildItem -Recurse -Filter ".git" -Directory -ErrorAction SilentlyContinue -Path $repoRootDir | ForEach-Object {
    $repoDir = $_.FullName -replace "\\.git$"
    SetLocation $repoDir

    git add .

    if (-not (git diff --cached --quiet)) {
        git commit -m "automatic commit"
        git push
    }
}