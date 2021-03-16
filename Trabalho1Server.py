#!usr/bin/python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 12345
sock.bind((udp_host, udp_port))
op = 0
while True:
    print("\nEsperando pelo cliente...")
    data, addr = sock.recvfrom(1024)
    Data = data.decode()

    if Data == "1" and op == 0:
        respo = "\nTelefone selecionado, tecle: \n1 - Saldo\n2 - Fatura"
        sock.sendto(respo.encode('utf-8'), addr)
        op = 1
        Data = "0"
    else:
        if Data == "2" and op == 0:
            respo = "\nInternet selecionada, tecle: \n1 - Consumo\n2 - Fatura"
            sock.sendto(respo.encode('utf-8'), addr)
            op = 2
            Data = "0"

    if Data == "1" and op == 1:
        respo = "\nSeu saldo é de 24 min de ligação restante"
        sock.sendto(respo.encode('utf-8'), addr)
        print("Voltando a tela inicial")
        op = 0
        Data = "0"
    else:
        if Data == "2" and op == 1:
            respo = "Sua fatura é de R$ 65,40"
            sock.sendto(respo.encode('utf-8'), addr)
            print("Voltando a tela inicial")
            op = 0
            Data = "0"
    if Data == "1" and op == 2:
        respo = "\nSeu consumo foi de 764 mb de internet"
        sock.sendto(respo.encode('utf-8'), addr)
        print("Voltando a tela inicial")
        op = 0
        Data = "0"
    else:
        if Data == "2" and op == 2:
            respo = "Sua fatura é de R$ 89,90"
            sock.sendto(respo.encode('utf-8'), addr)
            print("Voltando a tela inicial")
            op = 0
            Data = "0"
