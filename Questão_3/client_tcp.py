import socket
import os

# --- CONFIGURAÇÕES ---
TCP_IP = '127.0.0.1'
TCP_PORTA = 10410  # 5 primeiros dígitos do TIA
TAMANHO_BUFFER = 4096

def exibir_menu():
    print("\n" + "=" * 40)
    print("  MENU - Transferência de Arquivos")
    print("=" * 40)
    print("  [1] Enviar arquivo ao servidor")
    print("  [2] Ver arquivos recebidos pelo servidor")
    print("  [3] Sair")
    print("=" * 40)

def escolher_arquivo():
    """Pede ao usuário um caminho de arquivo válido."""
    while True:
        caminho = input("\n  Informe o caminho do arquivo: ").strip()
        if os.path.isfile(caminho):
            return caminho
        else:
            print(f"  [!] Arquivo não encontrado: '{caminho}'. Tente novamente.")

def enviar_arquivo(cliente, caminho):
    """Envia o arquivo para o servidor."""
    nome_arquivo = os.path.basename(caminho)
    tamanho = os.path.getsize(caminho)

    # Envia o comando com nome e tamanho
    comando = f'ENVIAR:{nome_arquivo}:{tamanho}'
    cliente.send(comando.encode('utf-8'))

    # Aguarda confirmação do servidor
    ack = cliente.recv(TAMANHO_BUFFER)
    if ack != b'PRONTO':
        print("  [!] Servidor não está pronto. Tente novamente.")
        return

    # Envia os bytes do arquivo
    enviado = 0
    with open(caminho, 'rb') as f:
        while True:
            chunk = f.read(TAMANHO_BUFFER)
            if not chunk:
                break
            cliente.send(chunk)
            enviado += len(chunk)

    print(f"  [✓] {enviado} bytes enviados. Aguardando confirmação...")

    # Aguarda confirmação de recebimento
    resposta = cliente.recv(TAMANHO_BUFFER)
    if resposta == b'OK':
        print(f"  [✓] Servidor confirmou o recebimento de '{nome_arquivo}'!")
    else:
        print("  [!] Resposta inesperada do servidor.")

# --- CONEXÃO ---
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"\n  Conectando a {TCP_IP}:{TCP_PORTA}...")

try:
    cliente.connect((TCP_IP, TCP_PORTA))
    print("  Conectado ao servidor!\n")
except ConnectionRefusedError:
    print("  [ERRO] Conexão recusada. O servidor está rodando?")
    exit()

# --- LOOP DO MENU ---
while True:
    exibir_menu()
    opcao = input("  Escolha uma opção: ").strip()

    if opcao == '1':
        caminho = escolher_arquivo()
        enviar_arquivo(cliente, caminho)

    elif opcao == '2':
        cliente.send(b'LISTAR')
        resposta = cliente.recv(TAMANHO_BUFFER).decode('utf-8')
        print(f"\n  Arquivos recebidos pelo servidor:\n{resposta}")

    elif opcao == '3':
        cliente.send(b'SAIR')
        print("\n  Conexão encerrada. Até logo!")
        break

    else:
        print("  [!] Opção inválida. Tente novamente.")

cliente.close()