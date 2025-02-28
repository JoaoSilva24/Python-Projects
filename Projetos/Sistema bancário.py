menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

Saldo = 0
Limite = 500
Extrato = ""
Número_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            Saldo += valor
            Extrato += f"Depósito: R$ (valor:.2f)\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opção == "s":
        valor = float(input("Informe o valor do saque: "))

        Excedeu_saldo = valor > Saldo

        Excedeu_limite = valor > Limite

        Excedeu_saques = Número_saques >= LIMITE_SAQUES

        if Excedeu_saldo:
            print("Operação falhou! Você não tem saldo o suficiente.")

        elif Excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif Excedeu_saques: 
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            Número_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")
    
    elif opção == "e":
        print("\n=========EXTRATO=========")
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\nSaldo: R$ {Saldo:.2f}")
        print("=============================")

    elif opção == "q":
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada")