import time
from pathlib import Path

# Diccionario que utilizaremos como memoria caché
cache = {}


def leer_archivo(ruta):

    # Verificamos si el archivo ya está almacenado en la caché
    if ruta in cache:

        print("\n🟢 CACHE HIT")
        print("El archivo ya está en memoria.")
        print("Leyendo desde la caché...")

        inicio = time.time()

        contenido = cache[ruta]

        fin = time.time()

        tiempo = fin - inicio

        print(f"Tiempo de lectura desde caché: {tiempo:.8f} segundos")

        return contenido

    # Si no está en la caché, debemos acceder al disco
    print("\n🔵 CACHE MISS")
    print("El archivo no está en memoria.")
    print("Leyendo desde el disco...")

    inicio = time.time()

    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    fin = time.time()

    tiempo = fin - inicio

    # Guardamos el contenido en la caché
    cache[ruta] = contenido

    print(f"Tiempo de lectura desde disco: {tiempo:.8f} segundos")
    print("Archivo almacenado en la caché.")

    return contenido


# Archivo de muestra junto al script
archivo = Path(__file__).resolve().parent / "archivo_grande.txt"
if not archivo.exists():
    archivo.write_text(
        "Datos de prueba para simular la lectura desde disco y la cache.\n" * 20000,
        encoding="utf-8",
    )


print("========================================")
print("       SIMULADOR DE MEMORIA CACHÉ")
print("========================================")

# Primera lectura
print("\nPRIMERA LECTURA")
leer_archivo(archivo)

# Segunda lectura
print("\nSEGUNDA LECTURA")
leer_archivo(archivo)

# Tercera lectura
print("\nTERCERA LECTURA")
leer_archivo(archivo)