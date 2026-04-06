capacidade = float(input("Qual a capacidade máxima do elevador(kg)?:"))
peso1 = float(input("Qual o peso da pessoa 1?: "))
peso2 = float(input("Qual o peso da pessoa 2?: "))
peso3 = float(input("Qual o peso da pessoa 3?: "))
peso4 = float(input("Qual o peso da pessoa 4?: "))
peso5 = float(input("Qual o peso da pessoa 5?: "))

total = peso1 + peso2 + peso3 + peso4 + peso5

if capacidade >= total:
    print("O elevador pode subir")
else:
    print("O elevador não pode subir, a carga máxima foi excedida")