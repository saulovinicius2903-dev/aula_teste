import random

n = 4

matriz = [[random.randint(1, 50) for i in range(n)] for i in range(n)]

print("Matriz Gerada:")
for linha in matriz:
    print(linha)

diagonal_secundaria = [matriz[i][n - 1 - i] for i in range(n)]
print("Diagonal Secundária:", diagonal_secundaria)
