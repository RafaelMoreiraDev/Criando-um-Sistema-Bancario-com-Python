#Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
# Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
# Para a primeira versão do sistema devemos implementar apenas 3 operações:
# depósito, saque e extrato.

#Deve ser possível depositar valores positivos para a minha conta bancária. 
# A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos
# nos preocupar em identificar qual é o número da agência e conta bancária. 
# Todos os depósitos devem ser armazenados em uma variável e exibidos na 
# operação de extrato.

#O sistema deve permitir realizar 3 saques diários com limite máximo de 
# R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema 
# deve exibir uma mensagem informando que não será possível sacar o dinheiro 
# por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos
# na operação de extrato.


#Essa operação deve listar todos os depósitos e saques realizados na conta.
# No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, 
# exibir a mensagem: Não foram realizadas movimentações.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
#1500.45 = R$ 1500.45

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
saldo = 0
limite = 500
saque = [] 
deposito = []
numero_saque = 0
LMITE_SAQUE = 3

while True:
    opcao=input(menu)
    
    if opcao == "d":
        print("Deposito")
        ndeposito=float(input("Digite o valor do deposito!"))
        if ndeposito >0:
            saldo+= ndeposito
            deposito.append(ndeposito) 
            extrato= f"Saque de R${saldo:1.2f}"
    elif opcao =="s":
        print("Sacar")
        nSaque=float(input("informe o valor do saque:"))
        if (numero_saque < LMITE_SAQUE) and (nSaque <= limite) and(nSaque <= saldo):
            saldo-=nSaque
            saque.append(nSaque)
            numero_saque += 1
            extrato= f"Saque de R${nSaque:1.2f}"
            print(extrato)
        else:
            print("Erro na operação!! Limite de saque diário atingido, ou saldo insuficiente!!")
    elif opcao == "e":
        print(" Extrato")
        for i in saque:
            print(f"Saque de R${i:1.2f}")
        for i in deposito:
            print(f"Deposito de R4{i:.2f}")
        print(saldo)
    elif opcao == "q":
         break
    else:
        print("Operação invalida, por favor selecione uma opção valida!!")
    