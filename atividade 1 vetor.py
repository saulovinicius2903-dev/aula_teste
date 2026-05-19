import random

vetor = []
for i in range(10):
    vetor.append(random.randint(1,50))

pares = 0
impares = 0

print("Vetor gerado: ",vetor)

for numero in vetor:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Total de números pares: ",pares)
print("Total de números ímpares: ",impares)
