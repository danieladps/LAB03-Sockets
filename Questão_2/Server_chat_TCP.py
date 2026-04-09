import socket

# --- CONFIGURAÇÕES ---
TCP_IP = '127.0.0.1'
TCP_PORTA = 10440  # 5 primeiros dígitos do TIA
TAMANHO_BUFFER = 1024

# --- INICIALIZAÇÃO ---
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((TCP_IP, TCP_PORTA))
servidor.listen(1)

print(f"Servidor disponível na porta {TCP_PORTA} e escutando...")

conn, addr = servidor.accept()
print(f"Cliente conectado: {addr}\n")
print("Digite QUIT para encerrar.\n")

# --- LOOP DE CHAT ---
while True:
    data = conn.recv(TAMANHO_BUFFER).decode('utf-8')
    print(f"Cliente: {data}")

    if data.upper() == 'QUIT':
        print("Cliente encerrou o chat.")
        break

    resposta = input("Você (servidor): ")
    conn.send(resposta.encode('utf-8'))

    if resposta.upper() == 'QUIT':
        print("Encerrando chat.")
        break

conn.close()
servidor.close()