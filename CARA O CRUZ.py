# JUEGO DE CRUZ-CARA - PROYECTO N°2

# Creamos la lista, la cual contiene Cara o Cruz
import random
lista = ["CARA","CRUZ"]

# Aleatoriamente se imprime en pantalla alguna de las 2 palabras de la lista
elemento = random.choice(lista)
print(elemento)

# Creamos el condicional 
if elemento == "CARA":
    print("Ha salido CARA")
else:
    print("Ha salido CRUZ")