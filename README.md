# 🔐 Password Manager

Un gerenciador de senhas seguro e modular desenvolvido em **Python**, projetado para armazenar, gerenciar e criptografar suas credenciais de forma local e simplificada.

---

## 📌 Sobre o Projeto

O **Password Manager** é uma aplicação focada na proteção e organização de dados sensíveis (usuários, senhas, serviços). Utilizando módulos criptográficos dedicados e uma arquitetura limpa, o sistema garante que suas informações permaneçam protegidas localmente contra acessos não autorizados.

### ✨ Principais Funcionalidades

- **🔐 Autenticação por Senha Mestre**: Acesso restrito garantido por uma senha principal configurada pelo usuário.
- **🛡️ Criptografia de Ponta a Ponta**: Armazenamento seguro de credenciais através de módulos de criptografia (`crypto.py`).
- **➕ Cadastro e Gestão de Credenciais**: Adicione, visualize, atualize e remova senhas por serviço/plataforma.
- **🎲 Gerador de Senhas Fortes**: Criação automática de senhas seguras com combinações personalizadas de caracteres.
- **📁 Arquitetura Modular**: Separação clara entre lógica de interface, gerenciamento de dados e operações criptográficas.

---

## 📂 Estrutura do Projeto

```text
Password_manager/
│
├── program/
│   ├── Password_manager.py       # Ponto de entrada e interface do usuário
│   ├── class_and_functions.py    # Classes de domínio e funções utilitárias
│   └── crypto.py                 # Algoritmos de criptografia e gerenciamento de chaves
│
├── .gitattributes                # Configurações do Git
├── .gitignore                    # Arquivos ignorados pelo controle de versão
├── LICENSE                       # Licença de uso do software
└── README.md                     # Documentação do projeto
```

### 🧩 Módulos do Sistema

1. **`Password_manager.py`**:
   - Coordena a execução da aplicação.
   - Exibe o menu interativo e processa os comandos digitados pelo usuário.

2. **`crypto.py`**:
   - Trata a derivação de chaves a partir da Senha Mestre.
   - Criptografa dados antes do salvamento e descriptografa somente no momento do acesso autorizado.

3. **`class_and_functions.py`**:
   - Contém as abstrações de dados (classes como `Account` / `Manager`) e rotinas de validação, formatação e persistência de arquivos.

---

## 🚀 Como Executar o Projeto

### 📋 Pré-requisitos

- **Python 3.8+** instalado.
- Dependência de criptografia (caso utilize a biblioteca `cryptography`):

```bash
pip install cryptography
```

### 🛠️ Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Password_manager.py.git
   cd Password_manager
   ```

2. **Acesse o diretório do programa:**
   ```bash
   cd program
   ```

3. **Execute o arquivo principal:**
   ```bash
   python Password_manager.py
   ```

---

## 💡 Fluxo de Funcionamento

```text
  [ Usuário ]
       │
       ▼
[ Password_manager.py ] ── (Interface / Menu)
       │
       ├──► [ class_and_functions.py ] ── (Lógica do Sistema e Registros)
       │
       └──► [ crypto.py ] ───────────── (Criptografia / Decodificação)
```

1. **Abertura:** O usuário insere a Senha Mestre.
2. **Autenticação:** O sistema valida a chave através das funções de `crypto.py`.
3. **Menu de Opções:** O usuário escolhe entre cadastrar, buscar, gerar ou excluir senhas.
4. **Persistência:** Todos os dados salvos passam obrigatoriamente pela camada de criptografia antes de serem gravados.

---

## 🛡️ Segurança e Boas Práticas

- **Não compartilhe sua Senha Mestre**: Ela é a chave primária para a descriptografia dos seus dados.
- **Armazenamento Local**: Seus dados ficam salvos exclusivamente na sua máquina local.
- **Ambiente Virtual**: Recomenda-se o uso de um `venv` do Python para isolar as dependências do projeto:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
  ```

---

## 📄 Licença

Este projeto está sob a licença definida no arquivo [LICENSE](LICENSE).

---

---
*Projeto desenvolvido para fins educacionais e de segurança da informação.*
