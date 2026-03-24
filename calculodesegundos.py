dia = int(input("Dias:"))
hora = int(input("Horas:"))
minuto = int(input("Minutos:"))
segundo = int(input("Segundos:"))
dia = dia * 24 * 60 * 60
hora = hora * 60 * 60
minuto = minuto *60
total = dia + hora + minuto + segundo
print("O total de segundos é:",total)
