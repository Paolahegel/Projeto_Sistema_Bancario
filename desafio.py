menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Informe o valor desejado para o depósito: "))

        if valor_deposito > 0:
             saldo += valor_deposito
             extrato += f"Depósito de R$ {valor_deposito: .2f}\n"
             print("Depósito realizado com sucesso")

        else:
            print("Operação falhou! Informe um valor válido!")

    elif opcao == 2:
         valor_saque = float
         print("Limite")

    # elif opcao == 3:
    #     print("Extrato")

    # elif opcao == 0:
    #     break

    # else:
    #     print("Operação inválida, selecione a operação desejada novamente.")
