import requests # Libreria para enviar peticiones

response=requests.get ('http://api.open-notify.org/astros.json') # Hacer una peticion get (get, post, put, delete)
json=response.json() # La respuesta se guarda como json
print (json) # Mostrar la variable json (recordad que es un str)


for people in json['people']:
    print (people['name'])