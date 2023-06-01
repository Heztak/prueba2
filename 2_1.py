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

# Definimos el nombre del archivo de texto que vamos a crear
txt_file = "endpoint.csv"

# Abrimos el archivo en modo escritura ('w') y lo asociamos a la variable 'file'
with open(txt_file, "w") as file:
    # Escribimos la primera línea del archivo, que contiene los encabezados de las columnas
    file.write("Author,Quote\n")

    # Iteramos sobre cada cita en la lista 'quotes'
    for q in quotes:
        # Escribimos en el archivo una línea que contiene el autor y la cita, separados por punto y coma
        file.write(f'"{q["author"]}";"{q["quote"]}"\n')

# Imprimimos un mensaje en la consola para indicar que el archivo está listo
print("Archivo Listo!")
