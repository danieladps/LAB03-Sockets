import socket

# --- CONFIGURAÇÕES ---
TCP_IP = '127.0.0.1'
TCP_PORTA = 10440  # 5 primeiros dígitos do TIA
TAMANHO_BUFFER = 1024

# --- CONEXÃO ---
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Tentando conectar a {TCP_IP}:{TCP_PORTA}...")

try:
    cliente.connect((TCP_IP, TCP_PORTA))
    print("Conectado ao servidor. Digite QUIT para encerrar.\n")
except ConnectionRefusedError:
    print("Erro: Conexão recusada. Verifique se o Servidor está ativo.")
    exit()

# --- LOOP DE CHAT ---
while True:
    mensagem = input("Você (cliente): ")
    cliente.send(mensagem.encode('utf-8'))

    if mensagem.upper() == 'QUIT':
        print("Encerrando chat.")
        break

    resposta = cliente.recv(TAMANHO_BUFFER).decode('utf-8')
    print(f"Servidor: {resposta}")

    if resposta.upper() == 'QUIT':
        print("Servidor encerrou o chat.")
        break

cliente.close()