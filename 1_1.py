# Importamos las librerías necesarias
import os
import re  # Para trabajar con expresiones regulares
from datetime import datetime, timedelta  # Para trabajar con fechas y horas

# Definimos una función que cuenta los intentos fallidos de inicio de sesión en una hora determinada
def count_failed_logins_in_hour(log_file_path, hour):
    # Definimos una expresión regular que coincide con las líneas de log que indican un intento fallido de inicio de sesión
    pattern = r'Failed password for .* from .* port'
    
    count = 0  # Inicializamos un contador de intentos fallidos de inicio de sesión
    # Abrimos el archivo de log para lectura
    with open(log_file_path, 'r') as file:
        # Leemos cada línea del archivo de log
        for line in file:
            # Si la línea coincide con nuestro patrón de intento fallido de inicio de sesión
            if re.search(pattern, line):
                # Extraemos la marca de tiempo de la línea de log
                timestamp_str = line[:15]
                # Convertimos la marca de tiempo a un objeto datetime
                timestamp = datetime.strptime(timestamp_str, '%b %d %H:%M:%S')
                # Ajustamos el año del timestamp para coincidir con el año actual
                timestamp = timestamp.replace(year=datetime.now().year)
                # Si el timestamp está dentro de la hora que estamos revisando
                if hour <= timestamp < hour + timedelta(hours=1):
                    # Incrementamos el contador de intentos fallidos de inicio de sesión
                    count += 1

    # Devolvemos el conteo de intentos fallidos de inicio de sesión
    return count

# Especificamos la ruta al archivo de registros de autenticación
log_file_path = '/var/log/secure'

# Obtenemos la hora actual
now = datetime.now()
# Extraemos la última hora cerrada basándonos en la hora actual
hour_to_check = datetime(now.year, now.month, now.day, now.hour)

# Si no estamos en la marca de la hora exacta
if now.minute > 0:
    # Retrocedemos a la última hora cerrada
    hour_to_check -= timedelta(hours=1)

# Llamamos a nuestra función para obtener el número de intentos fallidos de inicio de sesión en la última hora cerrada
failed_logins = count_failed_logins_in_hour(log_file_path, hour_to_check)

# Imprimimos el resultado
print(f"La cantidad de inicios de sesión fallidos en la última hora cerrada ({hour_to_check.strftime('%H:%M')} - {(hour_to_check + timedelta(hours=1)).strftime('%H:%M')}) fue: {failed_logins}")
