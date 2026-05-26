def soma(valor1, valor2):
    res = valor1 + valor2
    return res

def subtrair(valor1, valor2):
    res = valor1 - valor2
    return res

def multi(valor1, valor2):
    res = valor1 * valor2
    return res

def divisao(valor1, valor2):
    res = valor1 / valor2
    return res

def menu():
    print("--- CALCULADORA --- ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

# Programa Principal
while True:
    opcao = menu()
    if opcao == 5: break
    vlr1 = int(input("Digite o primeiro valor: "))
    vlr2 = int(input("Digite o segundo valor: "))
    if opcao == 1:
        result = soma(vlr1, vlr2)
    elif opcao == 2:
        result = subtrair(vlr1, vlr2)
    elif opcao == 3:
        result = multi(vlr1, vlr2)
    else:
        result  = divisao(vlr1, vlr2)
    print("Resultado:",result)
