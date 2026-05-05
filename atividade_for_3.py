somapares = 0
somaimpares = 0

for i in range(1,101,1):
    if i%2 == 0:
        somapares = somapares + i
    else:
        somaimpares = somaimpares + i

print("Soma números pares: ",somapares)
print("Soma números impares: ",somaimpares)
