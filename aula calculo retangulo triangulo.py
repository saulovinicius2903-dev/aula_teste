print("--- Escolha uma opção ---")
opcao = int(input("1 - Retângulo | 2 - Triângulo: "))

if opcao == 1:
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area1 = base * altura
    print("A área do retângulo é",area1)
    
elif opcao == 2:
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area2 = (base*altura)/2
    print("A área do triângulo",area2)
    
else:
    print("Opção inválida")