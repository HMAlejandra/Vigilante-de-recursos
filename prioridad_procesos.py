import psutil
import os
import math
import time
import sys


# -----------------------------------------
# CONFIGURACIÓN DE LA PRIORIDAD
# -----------------------------------------

if len(sys.argv) < 2:
    print("Debes indicar la prioridad.")
    print("Ejemplo:")
    print("python prioridad_procesos.py baja")
    print("python prioridad_procesos.py alta")
    sys.exit()


prioridad = sys.argv[1].lower()

proceso = psutil.Process(os.getpid())


# -----------------------------------------
# ASIGNAR PRIORIDAD
# -----------------------------------------

if prioridad == "baja":

    proceso.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    nombre_prioridad = "BAJA"

elif prioridad == "alta":

    proceso.nice(psutil.HIGH_PRIORITY_CLASS)
    nombre_prioridad = "ALTA"

else:

    print("Prioridad no válida.")
    print("Usa: baja o alta")
    sys.exit()


# -----------------------------------------
# CÁLCULO PESADO
# -----------------------------------------

print("========================================")
print("       PRIORIDAD DE PROCESOS")
print("========================================")

print(f"Proceso ID: {os.getpid()}")
print(f"Prioridad: {nombre_prioridad}")
print("Iniciando cálculo...\n")


inicio = time.time()

resultado = 0

for i in range(10_000_000):
    resultado += math.sqrt(i)


fin = time.time()

tiempo_total = fin - inicio


# -----------------------------------------
# RESULTADOS
# -----------------------------------------

print("Cálculo finalizado.")
print(f"Prioridad: {nombre_prioridad}")
print(f"Resultado: {resultado:.2f}")
print(f"Tiempo de ejecución: {tiempo_total:.2f} segundos")