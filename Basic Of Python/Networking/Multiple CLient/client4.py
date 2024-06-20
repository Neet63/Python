import socket

def client1_task():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    message = "Client 4: Hello, Server!"
    client.send(message.encode('utf-8'))
    response = client.recv(4096)
    print(f"Server responded with: {response.decode('utf-8')}")
    client.close()

if __name__ == "__main__":
    client1_task()
