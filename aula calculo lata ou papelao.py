opcao = (input("Se deseja calcular a lata de óleo, digite 1, se deseja a caixa de papelão, digite 2: "))
if opcao == '1':
    raio = float(input("Digite o raio da lata: "))
    altura = float(input("Digite a altura da lata: "))
    volumelata = 3.14159*raio**2*altura
    print("O volume da lata é",volumelata)

elif opcao == '2':
    altura2 = float(input("Digite a altura da caixa: "))
    largura = float(input("Digite a largura da caixa: "))
    comprimento = float(input("Digite o comprimento da caixa: "))
    volumecaixa = altura2*largura*comprimento
    print("O volume da caixa é",volumecaixa)
    
else:
    ("Opção inválida")