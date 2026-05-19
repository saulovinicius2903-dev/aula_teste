import random

vetor = []
for i in range(20):
    vetor.append(random.randint(1,50))

print("Vetor gerado: ",vetor)

multiplos = [numero for numero in vetor if numero % 5 == 0]

print("Números múltiplos de 5: ",multiplos)
