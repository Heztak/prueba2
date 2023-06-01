import psutil

# Obtener información de la CPU
cpu_usage = psutil.cpu_percent(interval=1)
cpu_count = psutil.cpu_count()

# Obtener información de la memoria
memory = psutil.virtual_memory()
memory_total = memory.total / (1024 ** 3)  # Convertir a gigabytes
memory_used = memory.used / (1024 ** 3)  # Convertir a gigabytes
memory_percent = memory.percent

# Obtener información del disco
disk = psutil.disk_usage('/')
disk_total = disk.total / (1024 ** 3)  # Convertir a gigabytes
disk_used = disk.used / (1024 ** 3)  # Convertir a gigabytes
disk_percent = disk.percent

# Obtener información de la red
net = psutil.net_io_counters()
net_bytes_sent = net.bytes_sent / (1024 ** 3)  # Convertir a gigabytes
net_bytes_received = net.bytes_recv / (1024 ** 3)  # Convertir a gigabytes

# Imprimir los resultados
print("Información de recursos del equipo:")
print(f"Uso de la CPU: {cpu_usage}%")
print(f"Número de CPUs: {cpu_count}")
print(f"Memoria total: {memory_total:.2f} GB")
print(f"Memoria usada: {memory_used:.2f} GB")
print(f"Porcentaje de uso de memoria: {memory_percent}%")
print(f"Espacio total en disco: {disk_total:.2f} GB")
print(f"Espacio utilizado en disco: {disk_used:.2f} GB")
print(f"Porcentaje de uso de disco: {disk_percent}%")
print(f"Bytes enviados por la red: {net_bytes_sent:.2f} GB")
print(f"Bytes recibidos por la red: {net_bytes_received:.2f} GB")