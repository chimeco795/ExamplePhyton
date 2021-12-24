# while normal

x=5
while x>0:
    x-=1
    print(x)

# while en una sola linea
x = 5
while x > 0: x-=1; print(x)

# while mientras una lista no este vacia, pop va eliminando el elemento
x = ["Uno", "Dos", "Tres"]
while x:
    
    print(x)
    x.pop(0)

# while con else
x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")