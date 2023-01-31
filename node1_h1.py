import dpkt
import time
import socket

# Create an OpenFlow header
def create_header():
    of = dpkt.openflow.OpenFlow()
    of.version = 1
    of.header_type = dpkt.openflow.OFPT_HELLO
    of.xid = 0
    return of.pack()

# Create 20 OpenFlow headers
headers = [create_header() for _ in range(20)]

# Send headers to node h2
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.0.0.2', 6653))
start = time.time()
for header in headers:
    sock.send(header)
end = time.time()

# Calculate elapsed time
elapsed = end - start

# Print results
print("Time elapsed: {:.2f} seconds".format(elapsed))
