numinicio = int(input("Digite o valor inicial: "))
numfinal = int(input("Digite o valor final: "))
divisivel = int(input("Digite um número para divísivel: "))

for i in range(numinicio, numfinal+1,1):
    resto = i % divisivel
    if resto == 0:
        print(i, "Valor divisivel por ",divisivel)
            