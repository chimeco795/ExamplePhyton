# En Python no existe el switch pero se puede simular de la siguiente manera

def switch(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)

res = switch ('suma',2,2)() # necesita de () para realizar la llamada a la función, ya que lo que se devuelve en realidad es una función lambda.
print ("El res: " + str( res) )