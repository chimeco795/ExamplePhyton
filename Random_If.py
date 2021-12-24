import random  # Asi se importa una libreria

machine= random.randint(1,3) # Se define el rango del random

guest=int(input("Pieda, papel o tijera \n")) # Se pide un dato y se cast a tipo INT

# Se crear un if, se utiliza tabulador para indicar el modulo de codigo
if machine == guest:
    print("Empate Machine " +str(machine)+" Guest "+ str(guest) ) # Se castea guest(int) a cadena(str)
else:
    print("Win")