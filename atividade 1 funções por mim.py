def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b

def exibir_menu():
    print("\n--- CALCULADORA ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    opcao = input("Escolha uma opção (1-5): ")
    return opcao

def executar_calculadora():
    while True:
        opcao = exibir_menu()
        
        if opcao == '5':
            print("Programa encerrado. Até mais!")
            break
            
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, digite apenas números válidos.")
                continue

            if opcao == '1':
                resultado = somar(num1, num2)
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcao == '2':
                resultado = subtrair(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcao == '3':
                resultado = multiplicar(num1, num2)
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcao == '4':
                resultado = dividir(num1, num2)
                print(f"Resultado: {resultado}")
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o programa
executar_calculadora()