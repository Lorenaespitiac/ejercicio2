
gravedad_en_marte = 3.72
gravedad_en_la_tierra = 9.81
gravedad_en_neptuno = 11.15

print("INGRESE SU PESO EN KG")
Peso_tierra= float(input("cual es mi peso "))

Resultado_peso_marte = (Peso_tierra/gravedad_en_la_tierra)*gravedad_en_marte

Resultado_peso_en_neptuno = (Peso_tierra/gravedad_en_la_tierra)*gravedad_en_neptuno

#print("{:.1f}".format(, Resultado_peso_marte))

#print("El resultado del peso en neptuno es  ", Resultado_peso_en_neptuno)

print("Mi peso en marte es {:.2f} kg y mi peso en neptuno es {:.2f} kg".format(Resultado_peso_marte, Resultado_peso_en_neptuno))
