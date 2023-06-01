# Importamos el módulo 'requests' para realizar solicitudes HTTP
import requests

# Definimos la URL desde donde vamos a obtener los datos
url = "https://dummyjson.com/quotes"

# Realizamos una solicitud GET a la URL y almacenamos la respuesta en la variable 'response'
response = requests.get(url)

# Extraemos los datos en formato JSON de la respuesta y los almacenamos en la variable 'data'
data = response.json()

# Extraemos la lista de citas del diccionario 'data' y la almacenamos en la variable 'quotes'
quotes = data["quotes"]

# Creamos un diccionario vacío para almacenar el recuento de palabras
word_counts = {}

# Iteramos sobre cada cita en la lista 'quotes'
for q in quotes:
    # Convertimos la cita a minúsculas y la dividimos en palabras individuales
    words = q["quote"].lower().split()
    
    # Iteramos sobre cada palabra en la lista 'words'
    for w in words:
        # Verificamos si la palabra ya está en el diccionario 'word_counts'
        if w in word_counts:
            # Si la palabra ya está en el diccionario, incrementamos su contador en 1
            word_counts[w] += 1
        else:
            # Si la palabra no está en el diccionario, la agregamos y establecemos su contador en 1
            word_counts[w] = 1

# Ordenamos el diccionario 'word_counts' en base al valor de los contadores de forma descendente
word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Iteramos sobre cada par (palabra, contador) en la lista 'word_counts'
for word, count in word_counts:
    # Imprimimos la palabra y su contador en la consola
    print(f"{word}: {count}")
