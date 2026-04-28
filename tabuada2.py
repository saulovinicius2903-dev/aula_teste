while True:
    num = int(input("Digite um número para tabuada: "))
    if num == 0:
        print("0 = encerrar")
        break
    Nmin = int(input("Digite o valor mínimo para a tabuada: "))
    Nmax = int(input("Digite o valor máximo para a tabuada: "))
    print("Tabuada do", num,"de",Nmin,"até",Nmax)
    
    i = Nmin
    while i <= Nmax:  
     res = num * i
     print(num," x ", i," = ",res)
     i += 1
    print("--- FIM DA TABUADA ---")