import random

#matriz 3x3 de números aleatórios
M = []
for i in range(3):
    M.append([])
    for j in range(3):
        M[i].append(random.randint(0,50))
print(M)

principal = M[0][0] + M[1][1] + M[2][2]
print(principal)
