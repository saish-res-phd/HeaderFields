import socket
import time

IP = '10.0.0.2' # node h2 IP address
PORT = 6634
HEADER_FIELDS = 20

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to node h2's IP and port
s.bind((IP, PORT))

# listen for incoming connections
s.listen(1)

# accept the connection from node h1
connected = False
start_time = time.time()
while not connected:
    try:
        conn, addr = s.accept()
        connected = True
    except socket.error:
        if time.time() - start_time > 10:
            print("Connection from node h1 failed")
            break
        time.sleep(1)

# receive the header fields
header_fields = []
while len(header_fields) < HEADER_FIELDS:
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= 1:
        start_time = current_time
        bandwidth = len(header_fields) * 1024 / elapsed_time
        header_fields = []
        print("Latency: {:.2f} seconds".format(elapsed_time))
        print("Bandwidth: {:.2f} KBps".format(bandwidth / 1024))
    try:
        data = conn.recv(1024)
        header_fields.append(data.decode())
    except socket.error:
        pass

# close the connection
conn.close()
