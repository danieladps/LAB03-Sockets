# LAB03 — Programação de Socket UDP e TCP

**Disciplina:** Redes de Computadores  
**Instituição:** Universidade Presbiteriana Mackenzie  
**Integrantes:** Daniela Pereira da Silva  - **RA:** 10410906
**Integrantes:** Guilherme Itihara - **RA:** 10440279

---

## 📋 Sobre o projeto

Este repositório contém as atividades do LAB03, que tem como objetivo aprender a programar e analisar sockets UDP e TCP, comparando o funcionamento de ambos os protocolos da camada de transporte.

---

## 📁 Estrutura dos arquivos

```
├── server_chat_tcp.py       # Servidor do chat TCP (Questão 2)
├── client_chat_tcp.py       # Cliente do chat TCP (Questão 2)
├── server_files_tcp.py      # Servidor de transferência de arquivos (Questão 3)
└── client_files_tcp.py      # Cliente com menu de transferência de arquivos (Questão 3)
```

---

## 💬 Questão 2 — Chat TCP

Chat simples entre cliente e servidor via socket TCP. Ambos os lados trocam mensagens até uma das partes enviar o comando **SAIR**, encerrando a conexão.

### Como executar

1. Execute primeiro o servidor:
```bash
python server_chat_tcp.py
```

2. Em outro terminal, execute o cliente:
```bash
python client_chat_tcp.py
```

> A porta utilizada é **10440** (primeiros 5 dígitos do TIA).

---

## 📂 Questão 3 — Transferência de Arquivos TCP

Aplicação cliente-servidor para transferência de arquivos via socket TCP. O cliente exibe um menu interativo onde o usuário escolhe o arquivo a enviar em tempo real — nenhum arquivo é predefinido no código.

### Funcionalidades

- **[1] Enviar arquivo** — o usuário informa o caminho de qualquer arquivo do computador e ele é transmitido ao servidor, que o salva na pasta `arquivos_recebidos/`
- **[2] Ver arquivos recebidos** — lista os arquivos que o servidor já recebeu
- **[3] Sair** — encerra a conexão entre cliente e servidor

### Como executar

1. Execute primeiro o servidor:
```bash
python server_files_tcp.py
```

2. Em outro terminal, execute o cliente:
```bash
python client_files_tcp.py
```

> A porta utilizada é **10440** (primeiros 5 dígitos do TIA).

---

## 🎥 Vídeos de demonstração

| Vídeo | Conteúdo | Link |
|-------|----------|------|
| Vídeo 1 | Questões 1 e 2 — Chat TCP | [Assistir no YouTube](https://youtu.be/jQS7zw-OsEQ?si=s4oHm6ZQbs2ufNoI) |
| Vídeo 2 | Questão 3 — Transferência de Arquivos | [Assistir no YouTube](https://youtu.be/_mu8sm5rc4M) |
