menu = """
Qual opção deseja realizar?

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>  """
deposito = 0
saldo = 1500
extrato = ''
saque = 3
qtd_saques = 0
limite_saque = 500

while True:
    opcao = int(input(menu))

    if  opcao == 1:
        deposito = float(input(f"Qual valor deseja depositar? \n"))
        if  deposito <= 0:
            print("Você deve depositar um valor maior que ZERO!")
        else:
            print(f"O valor de R${deposito:.2f} foi depositado com sucesso!")
        

    elif  opcao == 2:
        valor_saque = float(input("Qual valor deseja sacar? \n"))
        if valor_saque <= 0:
            print("Digite um valor real para o saque!")
        elif valor_saque > limite_saque:
            print(f"Valor máximo permitido para saque é de R$500.00!")

        total_saldo = valor_saque > saldo
        total_limite = valor_saque > limite_saque
        total_saques = qtd_saques >= saque


        if  total_saldo:
            print("Saldo insulficiente.")

        elif  total_limite:
            print("Valor do saque é maior que seu limite.")

        elif  total_saques:
            print("Você atingiu o limite de saques diário.")


        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"R$ {valor_saque:.2f}"
            qtd_saques += 1
        else:
            print("O valor que deseja sacar é inválido!")
       
    elif  opcao == 3:

        print("*****Extrato*****")
        if  extrato > '':
            print(f"O seu extrato é de R${saldo:.2f}")
       
    
    elif  opcao == 4:
        print("Operação finalizada!")
        break

    
    else:
        print("Opção inválida, digite a novamente")
    