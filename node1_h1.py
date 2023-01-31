import socket
import time

IP = '10.0.0.2' # node h2 IP address
PORT = 6634
HEADER_FIELDS = 20

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish a connection to node h2
connected = False
start_time = time.time()
while not connected:
    try:
        s.connect((IP, PORT))
        connected = True
    except socket.error:
        if time.time() - start_time > 10:
            print("Connection to node h2 failed")
            break
        time.sleep(1)

# send the header fields
for i in range(HEADER_FIELDS):
    s.send(str(i).encode())

# close the socket
s.close()
