import socket, ssl

HOST, PORT = '127.0.0.1', 4443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as bindsock:
    bindsock.bind((HOST, PORT))
    bindsock.listen(5)
    print(f"[Server] Listening on {HOST}:{PORT} ...")

    with context.wrap_socket(bindsock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(f"[Server] Connection from {addr}")
        data = conn.recv(4096)
        print("[Server] Received:", data.decode())
        conn.sendall(b"Hello secure client! This is the server.")
        conn.close()
