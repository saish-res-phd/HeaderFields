import dpkt
import time
import socket

# Receive headers from node h1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.0.0.1', 6653))
sock.listen(1)
conn, _ = sock.accept()

# Measure performance
received_headers = 0
start = time.time()
while received_headers < 20:
    header = conn.recv(8)
    received_headers += 1
end = time.time()

# Calculate elapsed time
elapsed = end - start

# Print results
print("Time elapsed: {:.2f} seconds".format(elapsed))
print("Bandwidth: {:.2f} MBps".format(20 * 8 / (10**6 * elapsed)))
