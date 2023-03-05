import socket 
import threading 

# Specify server port number, IP address, socket, and header (size of msg) 
HEADER = 64
PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


# Specify the family of IPs that the server accepts 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"New connection, {addr} connected.")
    connected = True

    while (connected):
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}] {msg}")
        if msg == DISCONNECT_MESSAGE:
                connected = False
        else:
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
            
    conn.close()


def start():
    server.listen()
    print(f"Server listening on {SERVER}")

    while (True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()

if __name__ == "__main__":
    start()
