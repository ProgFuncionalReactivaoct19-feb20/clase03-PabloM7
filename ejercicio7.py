"""
	Dada las siguientes placas, filtrar aquellas que pertenecen a las provincias de :

	Loja, Pichincha, Esmeraldas, Azuay, Imbabura
"""
def placa(x):
	#Esta variable permitira comparar solo con la primera letra de cada placa
	primer_caracter = x[0]
	#La lista que usaremos para evaluar
	iniciales_provincia = ["l", "p", "e", "a", "i"]
	#Condicion para comparar
	if primer_caracter in iniciales_provincia:
		return True
	else:
		return False
placas = ("lba-001", "gma-002", "azx-003", "ess-004", "oro-100", "mab-001", "iaj-002")
resultado = filter(placa, placas)
print(list(resultado))