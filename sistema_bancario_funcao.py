def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= saldo and valor <= limite and numero_saques < limite_saques:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
    else:
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
    return saldo, extrato

def deposito(saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    return saldo, extrato

def extrato(saldo, extrato, *, imprimir=True):
    if imprimir:
        print("\n================ EXTRATO ================")
        if extrato:
            for movimento in extrato:
                print(movimento)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

# Lista de usuários
usuarios = []

def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    # Adiciona usuário à lista
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco, 'saldo': 0, 'extrato': [], 'limite': 500, 'limite_saques': 3, 'numero_saques': 0})
    print("Usuário cadastrado com sucesso!")

# Função principal
def main():
    # Entrada de dados do usuário
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Informe o CPF (apenas números): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    # Criação do usuário
    criar_usuario(nome, data_nascimento, cpf, endereco)

    # Loop principal do programa
    while True:
        print("\n=== Menu ===")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                usuarios[-1]['saldo'], usuarios[-1]['extrato'] = deposito(usuarios[-1]['saldo'], valor, usuarios[-1]['extrato'])
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            if valor > 0:
                usuarios[-1]['saldo'], usuarios[-1]['extrato'] = saque(saldo=usuarios[-1]['saldo'], valor=valor, extrato=usuarios[-1]['extrato'], limite=usuarios[-1]['limite'], numero_saques=usuarios[-1]['numero_saques'], limite_saques=usuarios[-1]['limite_saques'])
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "3":
            extrato(saldo=usuarios[-1]['saldo'], extrato=usuarios[-1]['extrato'])

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
