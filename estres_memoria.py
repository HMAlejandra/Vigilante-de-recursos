import psutil
import time

# Límite de seguridad de memoria que utilizará el programa
LIMITE_MB = 1000

# Cada bloque tendrá aproximadamente 50 MB
BLOQUE_MB = 50

# Lista donde almacenaremos los bloques de memoria
memoria = []

print("========================================")
print("       ESTRÉS DE MEMORIA")
print("========================================")
print(f"Límite de seguridad: {LIMITE_MB} MB")
print("Presiona CTRL + C para detener.\n")


try:

    while True:

        # Calculamos cuánta memoria ha reservado nuestro programa
        memoria_usada = len(memoria) * BLOQUE_MB

        # Verificamos el límite de seguridad
        if memoria_usada >= LIMITE_MB:
            print("\n🛑 LÍMITE DE SEGURIDAD ALCANZADO")
            print(f"Memoria asignada: {memoria_usada} MB")
            break

        # Creamos un bloque de aproximadamente 50 MB
        bloque = "X" * (BLOQUE_MB * 1024 * 1024)

        # Guardamos el bloque en la lista
        memoria.append(bloque)

        # Consultamos la memoria del sistema
        memoria_sistema = psutil.virtual_memory()

        print(
            f"Memoria del programa: {memoria_usada + BLOQUE_MB} MB | "
            f"RAM del sistema: {memoria_sistema.percent}%"
        )

        time.sleep(1)


except KeyboardInterrupt:

    print("\n\n🛑 Programa detenido por el usuario.")


print("\nPrueba finalizada de forma segura.")