Nmin = int(input("Digite o valor inicial da sequência: "))
Nmax = int(input("Digite o valor final da sequência: "))
for i in range(Nmin, Nmax+1):
    resto = i%2
    if resto == 0:
        print(i," - Par")
    else:
        print(i," - Impar")
print("Obrigado por usar nosso sistema")

              