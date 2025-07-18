import textwrap

def menu():
    menu_texto = """
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar contas
    [7]\tListar usuários
    [8]\tSelecionar Conta
    [0]\tSair
    => """
    return input(textwrap.dedent(menu_texto))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "limite": 500,
            "extrato": "",
            "numero_saques": 0
        }

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
        
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def listar_usuarios(usuarios):
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return

    print("\n================ USUÁRIOS ================")
    for usuario in usuarios:
        linha = f"""\
            Nome:\t{usuario['nome']}
            CPF:\t{usuario['cpf']}
            Endereço:\t{usuario['endereco']}
        """
        print("-" * 50)
        print(textwrap.dedent(linha))
    print("========================================")

def selecionar_conta(contas):
    if not contas:
        print("\n@@@ Nenhuma conta foi criada ainda. Crie uma conta primeiro. @@@")
        return None

    print("\nSelecione uma das contas abaixo:")
    listar_contas(contas)
    
    try:
        numero_conta_selecionada = int(input("Digite o número da conta que deseja usar: "))
        for conta in contas:
            if conta["numero_conta"] == numero_conta_selecionada:
                print(f"\n=== Conta {numero_conta_selecionada} selecionada! Titular: {conta['usuario']['nome']} ===")
                return conta
        
        print("\n@@@ Conta não encontrada. Tente novamente. @@@")
        return None
    except ValueError:
        print("\n@@@ Entrada inválida. Por favor, digite apenas o número da conta. @@@")
        return None


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    usuarios = []
    contas = []
    conta_ativa = None

    while True:
        opcao = menu()

        if opcao == "1": 
            if not conta_ativa:
                print("\n@@@ Por favor, selecione uma conta primeiro! Use a opção [8]. @@@")
                continue
            
            valor = float(input("Informe o valor do depósito: "))
            novo_saldo, novo_extrato = depositar(conta_ativa['saldo'], valor, conta_ativa['extrato'])
            conta_ativa['saldo'] = novo_saldo
            conta_ativa['extrato'] = novo_extrato

        elif opcao == "2": 
            if not conta_ativa:
                print("\n@@@ Por favor, selecione uma conta primeiro! Use a opção [8]. @@@")
                continue

            valor = float(input("Informe o valor do saque: "))
            
            novo_saldo, novo_extrato, novo_num_saques = sacar(
                saldo=conta_ativa['saldo'],
                valor=valor,
                extrato=conta_ativa['extrato'],
                limite=conta_ativa['limite'],
                numero_saques=conta_ativa['numero_saques'],
                limite_saques=LIMITE_SAQUES,
            )
            
            conta_ativa['saldo'] = novo_saldo
            conta_ativa['extrato'] = novo_extrato
            conta_ativa['numero_saques'] = novo_num_saques

        elif opcao == "3": # Extrato
            if not conta_ativa:
                print("\n@@@ Por favor, selecione uma conta primeiro! Use a opção [8]. @@@")
                continue
            
            exibir_extrato(conta_ativa['saldo'], extrato=conta_ativa['extrato'])

        elif opcao == "4": # Novo Usuário
            criar_usuario(usuarios)

        elif opcao == "5": # Nova Conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)
            
        elif opcao == "7":
            listar_usuarios(usuarios)

        elif opcao == "8": 
            conta_ativa = selecionar_conta(contas)

        elif opcao == "0": 
            print("\nObrigado por utilizar nossos serviços! 👋")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
