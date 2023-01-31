import socket

IP = '10.0.0.2' # node h2 IP address
PORT = 6653
HEADER_FIELDS = 20

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to node h2
try:
    s.connect((IP, PORT))
except socket.error as e:
    print("Error connecting to node h2:", e)
    exit()

# send the header fields
for i in range(HEADER_FIELDS):
    try:
        s.send(str(i).encode())
    except socket.error as e:
        print("Error sending header field", i, ":", e)
        exit()

# close the connection
s.close()
