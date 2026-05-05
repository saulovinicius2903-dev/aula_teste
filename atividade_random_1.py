import random

cont = 1
while cont != 0:
    n1 = random.randint(0,10)
    n2 = random.randint(0,10)
    resposta = n1 * n2
    print("Número 1:",n1)
    print("Número 2:",n2)
    ent = int(input("Digite o resultado da multiplicação: "))
    if ent == resposta:
        print("ACERTOU!!")
    else:
        print("ERROU!!")
        
    print("Deseja tentar novamente? 1 para Sim / 0 para Não")
    cont = int(input(":"))
    