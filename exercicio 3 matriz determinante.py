import random

n = 3
matriz = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

print("Matriz 3x3:")
for linha in matriz: print(linha)

det_p = (matriz[0][0] * matriz[1][1] * matriz[2][2] +
         matriz[0][1] * matriz[1][2] * matriz[2][0] +
         matriz[0][2] * matriz[1][0] * matriz[2][1])

det_s = (matriz[0][2] * matriz[1][1] * matriz[2][0] +
         matriz[0][0] * matriz[1][2] * matriz[2][1] +
         matriz[0][1] * matriz[1][0] * matriz[2][2])

determinante = det_p - det_s
print(f"\nDeterminante: {determinante}")
