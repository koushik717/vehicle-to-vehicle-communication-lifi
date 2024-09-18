import socket
import threading

# Configuration
HOST = '127.0.0.1'
PORT = 65432

# Function to handle communication with a connected vehicle
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"Received message: {message}")
        conn.sendall(f"Message received: {message}".encode('utf-8'))
    conn.close()

# Main server function
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server listening on port", PORT)
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
