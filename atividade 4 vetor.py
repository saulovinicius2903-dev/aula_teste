import random

num = int(input("Digite o número divisor: "))

numeros = []
divisiveis = []

for i in range(21):
    #sortear números aleatórios
    sort = random.randint(1,50)
    #adicionar os números no vetor numeros
    numeros.append(sort)
    #se for divisivel por variavel num
    if sort%num == 0:
        #adicionar os números divisiveis no vetor divisiveis
        divisiveis.append(sort)
        
print("Vetor de números sorteados:")
print(numeros)
print("Vetor de números divisiveis por", num,":")
print(divisiveis)
    