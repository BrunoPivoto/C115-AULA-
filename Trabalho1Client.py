import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_host = socket.gethostname()
    udp_port = 12345
    msg = input("\nBom dia, envie:\n1- telefone\n2- internet\n3- sair\n\nOpção 1: ")
    if not msg != "3":
        print("Encerrando conexão...")
        sock.close()
        break
    else:
        sock.sendto(msg.encode(), (udp_host, udp_port))
        resp = sock.recv(1024)
        print(resp.decode('utf-8'))
        msg2 = input("\nOpção 2: ")
        sock.sendto(msg2.encode(), (udp_host, udp_port))
        resp = sock.recv(1024)
        print(resp.decode('utf-8'))
        print("Reiniciando...")
