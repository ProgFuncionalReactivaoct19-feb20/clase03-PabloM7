"""
	Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.
	
	Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala, Portoviejo, Macas
"""

ciudades = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala", "Portoviejo", "Macas"]
#Usamos la funcion lambda para encontrar el numero de caracteres de cada palabra y filtrar los pares
par= filter(lambda x: len(x)%2==0, ciudades)
print(list(par_impar))