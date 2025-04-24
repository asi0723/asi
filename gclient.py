import socket 

host = "192.168.254.106"
# print(host)
# print(type(host))
port = 7777

s = socket.socket()
s.connect((host, port))

data = s.recv(1024)
print(data.decode().strip())
while True:
    user_input = input("").strip()
    try:
        s.sendall(user_input.encode())
        reply = s.recv(1024).decode().strip()
        if "CORRECT!" in reply:
            print(reply)
            break
        print(reply)
        continue
    except ConnectionAbortedError as e:
        reply = s.recv(1024).decode().strip()
        print(reply)
        break
s.close()
