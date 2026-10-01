import psutil
import time
from datetime import datetime

UMBRAL_RAM = 80

print("========================================")
print("      VIGILANTE DE RECURSOS")
print("========================================")
print("Monitoreando CPU y memoria RAM...")
print("Presiona CTRL + C para detener.\n")


while True:

    # Obtiene el porcentaje de uso del procesador
    cpu = psutil.cpu_percent(interval=1)

    # Obtiene información de la memoria RAM
    memoria = psutil.virtual_memory()

    # Porcentaje de RAM utilizada
    ram = memoria.percent

    print(f"CPU: {cpu}% | RAM: {ram}%")

    # Verificamos si la RAM supera el 80%
    if ram > UMBRAL_RAM:

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        mensaje = (
            f"[{fecha}] ALERTA: "
            f"Uso de RAM: {ram}%\n"
        )

        # Guardamos la alerta en un archivo
        with open("alertas_ram.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje)

        print("⚠ ALERTA: La memoria RAM supera el 80%.")

    # Espera 2 segundos antes de volver a comprobar
    time.sleep(2)