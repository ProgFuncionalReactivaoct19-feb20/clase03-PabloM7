"""
	Ejercicios de funciones de orden superior
	@pablom7


datos = [1, 2, 10, 11, 12, 13]

resultado = []

for i in datos:
	if i%2==0:
		resultado.append(i)

print(resultado)
"""
# Aplicacion de funcion filter

datos = [1, 2, 10, 11, 12, 13]
resultado = filter(lambda x: x%2==0, datos)
print(resultado)
print(list(resultado))