$exclude = @("venv", "desktop_automation.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "desktop_automation.zip" -Force