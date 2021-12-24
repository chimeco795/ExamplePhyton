# Crear clase animal generica
class Animal:
    def __init__(self,especie, edad):
        self.especie=especie
        self.edad=edad
    
    # Metodo generico
    def  hablar(self): # self es un parámetro se utilizará como una referencia al objeto mismo. Es como this en c#
        #Metodo vacio
        pass # Le indica al programa que ignore esa condición y continúe ejecutando el programa como de costumbre

   #Metodo generico
    def caminar(self):
       print("Caminando ",type(self).__name__)

  # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


# Crear clase perro que hereda de clase animal
class Perro(Animal):
    pass


# Soy un Animal del tipo Perro
mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
mi_perro.caminar()
