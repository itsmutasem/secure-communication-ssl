import socket, ssl

HOST, PORT = '127.0.0.1', 4443

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print("[Client] TLS version:", ssock.version())
        ssock.sendall(b"Hello secure server! This is the client.")
        data = ssock.recv(4096)
        print("[Client] Received:", data.decode())
