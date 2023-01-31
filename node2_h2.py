# Import necessary libraries
import socket
import struct
import time

# Define IP and port
IP = '10.0.0.2'
PORT = 6653

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to IP and port
s.bind((IP, PORT))

# Listen for incoming connections
s.listen()

# Accept the incoming connection from h1
conn, addr = s.accept()

# Record the start time
start_time = time.time()

# Receive the binary data from h1
data = conn.recv(80)

# Unpack the binary data into header fields
ofp_header_fields = struct.unpack('!20L', data)

# Record the end time
end_time = time.time()

# Calculate the latency
latency = end_time - start_time

# Print the results
print("Received 20 OpenFlow header fields from h1")
print("Latency: ", latency, "seconds")

# Close the connection and socket
conn.close()
s.close()
