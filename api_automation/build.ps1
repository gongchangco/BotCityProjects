$exclude = @("venv", "api_automation.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "api_automation.zip" -Force