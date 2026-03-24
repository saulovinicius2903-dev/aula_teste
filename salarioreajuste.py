salario = float(input("Informe seu salario:"))
reajuste = float(input("Informe o reajuste(%):"))
reajuste = reajuste/100
valorreajuste = salario * reajuste
novosalario = salario + valorreajuste
print("Seu salario é:",novosalario)

