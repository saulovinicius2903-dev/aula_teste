import random

print("1 para Ordem normal | 2 para Ordem inversa")
opcao = int(input("Digite a opção desejada: "))

#gerar vetor de números aleatorios
vetor = []
for i in range(10):
    vetor.append(random.randint(1,50))
    
#percorrer o vetor na ordem escolhida
if opcao == 1:
    #percorrer na ordem normal
    for i in range(0,len(vetor),1):
        print(vetor[i],end=',')
#percorrer ordem inversa
else:
    for i in range(len(vetor)-1,-1,-1):
        print(vetor[i], end=',')
