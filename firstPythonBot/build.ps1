$exclude = @("venv", "firstPythonBot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "firstPythonBot.zip" -Force