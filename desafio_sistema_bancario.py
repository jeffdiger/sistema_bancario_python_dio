menu = """

====== BANCO DIGITAL DO JEFFERSON =======

     [d] Deposito
     [s] Saque
     [e] Extrato
     [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Não é possível depositar valores negativos.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não há saldo suficiente.")

        elif excedeu_limite:
            print("Valor do saque excedeu o permitido.")

        elif excedeu_saques:
            print("Saques diários excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Não é possível sacar valores negativos.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Conta sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("Agradecemos por utilizar nossos serviços, tenha um bom dia!")
        break

    else:
        print("Comando inválido, por favor selecione novamente a operação desejada.")