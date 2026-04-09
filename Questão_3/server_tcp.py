import socket
import os

# --- CONFIGURAÇÕES ---
TCP_IP = '127.0.0.1'
TCP_PORTA = 10410  # 5 primeiros dígitos do TIA
TAMANHO_BUFFER = 4096
PASTA_RECEBIDOS = "arquivos_recebidos"

# Garante que a pasta de destino existe
os.makedirs(PASTA_RECEBIDOS, exist_ok=True)

def receber_arquivo(conn, nome_arquivo, tamanho):
    """Recebe os bytes do arquivo e salva na pasta de recebidos."""
    caminho = os.path.join(PASTA_RECEBIDOS, nome_arquivo)
    recebido = 0

    with open(caminho, 'wb') as f:
        while recebido < tamanho:
            chunk = conn.recv(min(TAMANHO_BUFFER, tamanho - recebido))
            if not chunk:
                break
            f.write(chunk)
            recebido += len(chunk)

    print(f"  [✓] Arquivo '{nome_arquivo}' recebido ({recebido} bytes) → salvo em '{PASTA_RECEBIDOS}/'")

def listar_arquivos():
    """Retorna lista dos arquivos já recebidos."""
    arquivos = os.listdir(PASTA_RECEBIDOS)
    if not arquivos:
        return "  (nenhum arquivo recebido ainda)"
    return "\n".join(f"  - {a}" for a in arquivos)

# --- INICIALIZAÇÃO DO SERVIDOR ---
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((TCP_IP, TCP_PORTA))
servidor.listen(1)

print("=" * 45)
print(f"  Servidor de Arquivos TCP")
print(f"  Porta: {TCP_PORTA} | Aguardando cliente...")
print("=" * 45)

conn, addr = servidor.accept()
print(f"\n  Cliente conectado: {addr}\n")

# --- LOOP PRINCIPAL ---
while True:
    # Recebe o comando do cliente
    try:
        comando = conn.recv(TAMANHO_BUFFER).decode('utf-8').strip()
    except ConnectionResetError:
        print("\n  Conexão encerrada pelo cliente.")
        break

    if not comando:
        continue

    if comando == 'SAIR':
        print("\n  Cliente encerrou a conexão.")
        break

    elif comando == 'LISTAR':
        lista = listar_arquivos()
        conn.send(lista.encode('utf-8'))

    elif comando.startswith('ENVIAR:'):
        # Formato: ENVIAR:<nome_arquivo>:<tamanho_em_bytes>
        partes = comando.split(':', 2)
        nome_arquivo = partes[1]
        tamanho = int(partes[2])

        # Confirma que está pronto para receber
        conn.send(b'PRONTO')

        receber_arquivo(conn, nome_arquivo, tamanho)

        # Confirma recebimento ao cliente
        conn.send(b'OK')

    else:
        conn.send(b'COMANDO_INVALIDO')

conn.close()
servidor.close()
print("\n  Servidor encerrado.")