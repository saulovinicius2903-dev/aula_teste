salario = float(input("Digite seu salário bruto mensal: R$ "))

if salario <= 2428.80:
    aliquota = 0
    deducao = 0

elif salario <= 2826.65:
    aliquota = 0.075
    deducao = 182.16

elif salario <= 3751.05:
    aliquota = 0.15
    deducao = 394.16

elif salario <= 4664.68:
    aliquota = 0.225
    deducao = 675.49

else:
    aliquota = 0.275
    deducao = 908.73

imposto = (salario * aliquota) - deducao

if salario <= 5000:
    imposto = 0
elif salario <= 7350:
    reducao = 978.62 - (0.133145 * salario)
    if reducao > 0:
        imposto -= reducao

if imposto < 0:
    imposto = 0

salario_liquido = salario - imposto

print("--- RESULTADO ---")
print(f"Salário bruto: R$ {salario:.2f}")
print(f"Alíquota aplicada: {aliquota*100:.1f}%")
print(f"Desconto IRRF: R$ {imposto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")

if imposto == 0:
    print("Você não paga o imposto!")

else:
    print("Vai ter que pagar imposto!")