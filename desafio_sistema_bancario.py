menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """

saldo = 0
limite = 500
extrato = []

LIMITE_SAQUES = 3
numero_saques = 0

def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor <= saldo and valor <= limite and numero_saques < LIMITE_SAQUES:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
    else:
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

def exibir_extrato():
    global saldo, extrato
    print("\n================ EXTRATO ================")
    if extrato:
        for movimento in extrato:
            print(movimento)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            depositar(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        if valor > 0:
            sacar(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        exibir_extrato()

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
