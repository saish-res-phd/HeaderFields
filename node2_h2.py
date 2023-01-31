import socket
import time

IP = '10.0.0.2' # node h2 IP address
PORT = 12345
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
for i in range(HEADER_FIELDS):
    data = conn.recv(1024)
    header_fields.append(data.decode())

# close the connection
conn.close()

# measure the performance
latency = time.time() - start_time
bandwidth = HEADER_FIELDS * 1024 / latency

# display the results
print("Latency:", latency)
print("Bandwidth:", bandwidth)
