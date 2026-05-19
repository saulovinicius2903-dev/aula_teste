import random

vetor = []
for i in range(20):
    vetor.append(random.randint(1,50))

soma_pares = 0
qtd_pares = 0

print("Vetor gerado: ",vetor)

for numero in vetor:
    if numero % 2 == 0:
        soma_pares += numero
        qtd_pares += 1

if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print("Quantidade de números pares: ",qtd_pares)
    print(f"Média dos números pares: {media_pares:.2f}")
else:
    print("Nenhum número par foi gerado.")
