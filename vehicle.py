import socket

# Configuration
HOST = '127.0.0.1'
PORT = 65432

# Function to send a message to the server
def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

# Simulate vehicle behavior
def vehicle_simulation():
    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        send_message(message)

if __name__ == "__main__":
    vehicle_simulation()
