# Sistema Bancário V2: Otimização com Funções em Python

## 📜 Sobre o Projeto

Este projeto aprimora uma versão inicial de um sistema bancário, refatorando o código para utilizar funções Python. O objetivo principal é otimizar a estrutura, aumentar a eficiência e facilitar a manutenção do sistema. As operações de depósito, saque, extrato, cadastro de usuários e criação de contas bancárias foram modularizadas em funções específicas, aplicando conceitos de argumentos posicionais e nomeados para uma implementação mais robusta e elegante.

## ✨ Funcionalidades

O sistema implementa as seguintes operações:

-   **Saque:** Permite que o usuário retire um valor de sua conta.
-   **Depósito:** Permite que o usuário adicione um valor à sua conta.
-   **Extrato:** Exibe o histórico de transações da conta.
-   **Criar Usuário:** Cadastra um novo usuário no sistema.
-   **Criar Conta Corrente:** Cria uma nova conta bancária vinculada a um usuário existente.
-   **Listar Contas:** Exibe todas as contas cadastradas no sistema.
-   **Inativar Conta:** (Funcionalidade futura a ser implementada).

## 🛠️ Estrutura e Regras de Negócio

### Funções e Seus Argumentos

A refatoração do código resultou nas seguintes funções com regras específicas de passagem de argumentos:

-   `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`
    -   **Argumentos:** Todos os argumentos são obrigatórios e devem ser passados por nome (`keyword-only`).
    -   **Retorno:** `(saldo, extrato)` - Uma tupla contendo o novo saldo e o extrato atualizado.

-   `depositar(saldo, valor, extrato, /)`
    -   **Argumentos:** Todos os argumentos são obrigatórios e devem ser passados por posição (`positional-only`).
    -   **Retorno:** `(saldo, extrato)` - Uma tupla contendo o novo saldo e o extrato atualizado.

-   `exibir_extrato(saldo, /, *, extrato)`
    -   **Argumentos:** `saldo` é um argumento posicional (`positional-only`), enquanto `extrato` é um argumento nomeado (`keyword-only`).
    -   **Ação:** Exibe o histórico de transações e o saldo atual da conta.

-   `criar_usuario(usuarios)`
    -   **Argumentos:** Recebe a lista de usuários cadastrados.
    -   **Lógica:** Solicita nome, data de nascimento, CPF e endereço. O CPF é validado para garantir que seja único. Apenas os números do CPF são armazenados. O endereço segue o formato: `Logradouro, nro - bairro - cidade/sigla estado`.

-   `criar_conta_corrente(agencia, numero_conta, usuarios)`
    -   **Argumentos:** Recebe o número da agência (`0001`), o número da próxima conta e a lista de usuários.
    -   **Lógica:** O número da conta é sequencial, iniciando em 1. A função vincula a nova conta a um usuário existente através do CPF. Uma conta não pode existir sem um usuário.

-   `listar_contas(contas)`
    -   **Argumentos:** Recebe a lista de contas cadastradas.
    -   **Ação:** Exibe uma lista formatada com a agência, o número da conta e o nome do titular de cada conta.

### Estrutura de Dados

-   **Usuários:** Armazenados em uma lista de dicionários. Cada usuário é composto por:
    -   `nome` (string)
    -   `data_nascimento` (string)
    -   `cpf` (string, apenas números)
    -   `endereco` (string)

-   **Contas:** Armazenadas em uma lista de dicionários. Cada conta é composta por:
    -   `agencia` (string, valor fixo "0001")
    -   `numero_conta` (inteiro, sequencial)
    -   `usuario` (dicionário contendo os dados do usuário vinculado)

## 🚀 Como Executar

1.  **Pré-requisitos:**
    -   Certifique-se de ter o Python 3.8 ou superior instalado em sua máquina (necessário para os argumentos `positional-only`).

2.  **Clone o repositório (opcional, se estiver no GitHub):**
    ```bash
    git clone [https://seu-link-para-o-repositorio.git](https://seu-link-para-o-repositorio.git)
    cd seu-repositorio
    ```

3.  **Execute o script Python:**
    ```bash
    python nome_do_seu_arquivo.py
    ```

4.  **Interaja com o menu:**
    -   O programa apresentará um menu no terminal. Digite o número da opção desejada e pressione Enter para interagir com o sistema.