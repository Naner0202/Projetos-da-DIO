import datetime
hoje = datetime.date.today()

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
-> '''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 0

while True:
    opcao = input(menu)
    if opcao == 'd':
        print('Depósito'.center(50, '-'))
        valorDeposito = float(input("Digite o valor a ser depositado: "))
        if valorDeposito < 0:
            print('Não é possível realizar a operação.')
        else:
            saldo += valorDeposito
            extrato += "Valor depositado no dia {}: R$ {:.2f}\n".format(hoje, valorDeposito)
            print('Valor depositado com sucesso!')

    elif opcao == 's':
        print('Saque'.center(50, '-'))
        valorSaque = float(input('Digite o valor a ser sacado: '))
        if saldo < valorSaque:
            print('Saldo insuficiente para realizar a operação.\n')
        elif (valorSaque <= 500 and valorSaque > 0) and limite_saques < 3 and saldo > valorSaque:
            saldo -= valorSaque
            extrato += "Valor sacado no dia {}: R$ {:.2f}\n".format(hoje, valorSaque)
            limite_saques += 1
            print('Valor sacado com sucesso!')
        else:
            print('Não é possível realizar a operação.\n')

    elif opcao == 'e':
        print('Extrato'.center(50, '-'))
        print('Não foram realizadas transações.'if not extrato else extrato)
        print('Saldo atual: R$ {:.2f}'.format(saldo))

    elif opcao == 'q':
        print('Obrigado por utilizar nossos serviços! ')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')
