import random

n = 4

matriz = [[random.randint(1, 50) for _ in range(n)] for _ in range(n)]

print("Matriz Gerada:")
for linha in matriz:
    print(linha)

diagonal_principal = [matriz[i][i] for i in range(n)]
print("Diagonal Principal:", diagonal_principal)
