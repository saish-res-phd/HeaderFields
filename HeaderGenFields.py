# Import necessary libraries
import socket
import struct

# Define IP and port
IP = '10.0.0.2' # IP of h2
PORT= 6633

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to h2
s.connect((IP,PORT))

# Generate 20 OpenFlow header fields
ofp_header_fields = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Pack the header fields into binary data
data = struct.pack('!20L', *ofp_header_fields)

# Send the binary data to h2
s.sendall(data)

# Close the socket
s.close()
