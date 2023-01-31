import ryu.ofproto.ofproto_v1_0 as ofp
import socket
import time

# Create a Ryu OpenFlow header
def create_header():
    msg = ryu.ofproto.ofproto_v1_0_parser.OFPHello(
        datapath_id=0,
        n_buffers=0,
        n_tables=0,
        capabilities=0,
        actions=0
    )
    return msg

# Create 20 Ryu OpenFlow headers
headers = [create_header() for _ in range(20)]

# Send headers to node h2
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.0.0.2', 6653))
start = time.time()
for header in headers:
    sock.send(header.buf)
end = time.time()

# Calculate elapsed time
elapsed = end - start

# Print results
print("Time elapsed: {:.2f} seconds".format(elapsed))
