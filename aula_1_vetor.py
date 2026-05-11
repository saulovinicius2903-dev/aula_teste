L = []
print("L", L)

L1 = [0] * 5
print("L1", L1)

L2 = [1, 2, 3, 4, 5]
print("L2", L2[3])

L3 = ["a", "b", "c"]
print("L3", L3)

L4 = list("TSI" + "356")
print("L4-1", L4)

L5 = [15, 8, 9]
print("L5-1", L5)
L5[0] = 7
print("L5-2", L5[0])

#QUANTIDADE DE ELEMENTOS
print("L4-2", len(L4))

#PERCORRER LISTA
for i  in L4:
    print("L4-3", i)

for i in range(len(L4)):
    print("L4-4", L4[i])
    
#ADICIONAR ELEMENTOS
L6 = [0, 0, 0, 0, 0]
L6[0] = int(input("[L6] Digite um valor: "))
print("L6", L6)

L7 = []
for i in range(1,3):
    L7.append(int(input("[L7] Digite um valor: ")))
print("L7-1", L7)

L7.insert(1,80)
print("L7-2", L7)

#ADICIONAR ALEATÓRIO
from random import randint

L8 = []
for i in range(5):
    L8.append(randint(0,50))
print("L8", L8)


