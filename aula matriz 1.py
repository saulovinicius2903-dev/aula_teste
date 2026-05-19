import random

# Matrizes
M = [[1,2,3],[4,5,7]]
print (M) #imprime a matriz

print(M[1][1]) # acessar elemento
M1 = [0] * 3
print(M1)

for i in range(3):
    M1[i] = [0] * 3
print(M1)

#percorrendo matrizes
M2=[[10,20,30], [40,50,60]]
for i in range(2): #linha
    for j in range(3): #coluna
        (M2[i][j]) = random.randint(0,50)
print(M2)

#adicionar elementos
M3=[]
for i in range(3):
    M3.append([])
    for j in range(3):
        M3[i].append(int(input("Digite um número:")))
print(M3)