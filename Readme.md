Proyecto de Sistemas Operativos

Vigilante de Recursos, Caché, Memoria Virtual y Scheduling

Proyecto práctico desarrollado en Python para comprender y experimentar
con diferentes conceptos fundamentales de los Sistemas Operativos,
incluyendo gestión de recursos, jerarquía de memoria, memoria virtual y
planificación de procesos.

📌 Descripción del proyecto

Este proyecto reúne cuatro ejercicios prácticos que permiten observar,
mediante programas desarrollados en Python, cómo un sistema operativo
administra los recursos de hardware y los procesos.

Los ejercicios desarrollados son:

Vigilante de Recursos --- monitoreo de CPU y RAM.

Simulador de Memoria Caché --- comparación conceptual entre
acceso a disco y acceso a memoria.

Estrés de Memoria y Memoria Virtual --- asignación controlada de
memoria.

Prioridad de Procesos --- experimentación con la planificación y
prioridad de procesos.

El proyecto fue desarrollado y probado utilizando Python y Visual
Studio Code.

🎯 Objetivo general

Implementar diferentes programas en Python que permitan comprender de
manera práctica conceptos relacionados con la administración de recursos
y la gestión de procesos y memoria realizada por un sistema operativo.

Objetivos específicos

Monitorear en tiempo real el consumo de CPU y memoria RAM.

Generar registros cuando el uso de RAM supere un umbral establecido.

Simular el funcionamiento de una caché utilizando estructuras de
datos en memoria.

Comparar los tiempos de acceso a un archivo desde disco y desde una
caché en RAM.

Experimentar de forma controlada con la asignación de memoria.

Observar el comportamiento de la memoria del sistema durante una
prueba de estrés.

Modificar la prioridad de un proceso y observar su comportamiento
bajo diferentes niveles de prioridad.

🛠️ Tecnologías utilizadas

Python 3

Visual Studio Code

psutil

Git / GitHub

Windows Task Manager para observar el comportamiento de los
recursos del sistema.

Instalación de la dependencia

El proyecto utiliza la librería psutil.

Instalarla mediante:

pip install psutil

También puede utilizarse:

python -m pip install psutil

📁 Estructura del proyecto

Vigilan de recursos/
│
├── vigilante_recursos.py
├── simulador_cache.py
├── estres_memoria.py
├── prioridad_procesos.py
│
├── alertas_ram.txt
└── archivo_grande.txt

1. 🖥️ Vigilante de Recursos

Concepto

Gestión y monitoreo de recursos del sistema.

Objetivo

Crear un programa capaz de consultar continuamente el porcentaje de
utilización de la CPU y la memoria RAM, generando una alerta cuando el
consumo de RAM supere un umbral determinado.

Funcionamiento

El programa utiliza la librería psutil para obtener información del
sistema.

La CPU se consulta mediante:

psutil.cpu_percent()

La información de la memoria RAM se obtiene mediante:

psutil.virtual_memory()

Se estableció un umbral de:

UMBRAL_RAM = 80

Cuando el porcentaje de RAM supera el 80 %, el programa genera una
alerta y almacena la información en:

alertas_ram.txt

Ejecución

python vigilante_recursos.py

Ejemplo de salida

========================================
      VIGILANTE DE RECURSOS
========================================
Monitoreando CPU y memoria RAM...

CPU: 12.5% | RAM: 63.2%
CPU: 8.7% | RAM: 63.5%
CPU: 15.1% | RAM: 63.4%

Cuando se supera el umbral:

⚠ ALERTA: La memoria RAM supera el 80%.

📸 Evidencias --- Vigilante de Recursos

Captura 1 --- Código fuente

Insertar aquí la captura del archivo vigilante_recursos.py.

Descripción: Código utilizado para obtener el porcentaje de CPU y
RAM y generar las alertas.

CAPTURA AQUÍ

Captura 2 --- Monitoreo en tiempo real

Insertar aquí la captura de la terminal ejecutando
vigilante_recursos.py.

Descripción: Ejecución del programa mostrando el porcentaje de CPU y
RAM.

CAPTURA AQUÍ

Captura 3 --- Administrador de tareas

Insertar aquí la captura del Administrador de tareas de Windows.

Descripción: Visualización del consumo de CPU y memoria RAM durante
la ejecución del programa.

CAPTURA AQUÍ

Captura 4 --- Registro de alertas

Insertar aquí la captura del archivo alertas_ram.txt.

Descripción: Registro generado automáticamente cuando se supera el
umbral establecido.

CAPTURA AQUÍ

2. 💾 Simulador de Memoria Caché

Concepto

Jerarquía de memoria y optimización de acceso a datos.

Objetivo

Simular el principio de funcionamiento de una caché utilizando un
diccionario de Python para almacenar en memoria el contenido de un
archivo después de su primera lectura.

Funcionamiento

En la primera lectura, el archivo no se encuentra en la caché:

CACHE MISS

Por lo tanto, el programa debe acceder al disco y posteriormente
almacenar el contenido en memoria.

En las siguientes lecturas:

CACHE HIT

el contenido se obtiene directamente desde el diccionario utilizado como
caché.

La caché se representa mediante:

cache = {}

La comprobación se realiza mediante:

if ruta in cache:

El tiempo de ejecución se mide utilizando:

time.time()

Ejecución

python simulador_cache.py

Flujo de funcionamiento

Primera lectura
      ↓
¿Está en caché?
      ↓
    NO
      ↓
Leer desde disco
      ↓
Guardar en caché
      ↓
      Fin

Siguiente lectura
      ↓
¿Está en caché?
      ↓
    SÍ
      ↓
Leer desde memoria

Nota: Este programa es una simulación educativa. El diccionario de
Python no representa literalmente una caché física L1 o L2 del
procesador; representa el principio de evitar accesos repetidos a un
medio de almacenamiento más lento.

📸 Evidencias --- Simulador de Caché

Captura 1 --- Código fuente

Insertar aquí la captura de simulador_cache.py.

Descripción: Código encargado de implementar la caché mediante un
diccionario.

CAPTURA AQUÍ

Captura 2 --- Archivo utilizado

Insertar aquí la captura de archivo_grande.txt dentro del
proyecto.

Descripción: Archivo utilizado para realizar las pruebas de lectura.

CAPTURA AQUÍ

Captura 3 --- Primera lectura / Cache Miss

Insertar aquí la captura de la terminal mostrando CACHE MISS.

Descripción: Primera lectura del archivo, realizada directamente
desde el disco.

CAPTURA AQUÍ

Captura 4 --- Lecturas posteriores / Cache Hit

Insertar aquí la captura mostrando CACHE HIT y los tiempos de
lectura.

Descripción: Lecturas posteriores realizadas desde la caché.

CAPTURA AQUÍ

3. 🧠 Estrés de Memoria y Memoria Virtual

Concepto

Memoria virtual, administración de memoria y paginación.

Objetivo

Crear una prueba controlada que asigne progresivamente bloques de
memoria y permita observar cómo aumenta el consumo de RAM del sistema.

Funcionamiento

El programa utiliza una lista para conservar los bloques de memoria
asignados:

memoria = []

Cada bloque ocupa aproximadamente:

50 MB

El programa agrega bloques progresivamente:

memoria.append(bloque)

Además, se estableció un límite de seguridad:

LIMITE_MB = 1000

Cuando se alcanza dicho límite, el programa finaliza automáticamente.

Ejecución

python estres_memoria.py

Ejemplo de salida

Memoria del programa: 50 MB | RAM del sistema: 61.2%
Memoria del programa: 100 MB | RAM del sistema: 61.8%
Memoria del programa: 150 MB | RAM del sistema: 62.5%

Al alcanzar el límite:

🛑 LÍMITE DE SEGURIDAD ALCANZADO
Memoria asignada: 1000 MB

Prueba finalizada de forma segura.

Importante: La asignación de memoria no garantiza que Windows
utilice inmediatamente el archivo de paginación. El sistema operativo
decide cuándo necesita utilizar mecanismos de memoria virtual según la
presión de memoria y otras condiciones.

📸 Evidencias --- Estrés de Memoria

Captura 1 --- Código fuente

Insertar aquí la captura de estres_memoria.py.

Descripción: Código utilizado para realizar la asignación controlada
de memoria.

CAPTURA AQUÍ

Captura 2 --- Programa ejecutándose

Insertar aquí la captura de la terminal mientras aumenta la memoria
asignada.

Descripción: Incremento progresivo de la memoria utilizada por el
programa.

CAPTURA AQUÍ

Captura 3 --- Administrador de tareas

Insertar aquí la captura de Rendimiento → Memoria en Windows.

Descripción: Comportamiento de la memoria RAM del sistema durante la
prueba.

CAPTURA AQUÍ

Captura 4 --- Límite de seguridad

Insertar aquí la captura del programa mostrando que alcanzó el
límite establecido.

Descripción: Finalización controlada para evitar un consumo excesivo
de memoria.

CAPTURA AQUÍ

4. ⚙️ Prioridad de Procesos

Concepto

Planificación de procesos (Scheduling) y prioridades del sistema
operativo.

Objetivo

Ejecutar el mismo cálculo matemático utilizando diferentes prioridades
de proceso para observar cómo el sistema operativo administra los
procesos.

Funcionamiento

El programa utiliza psutil para establecer diferentes niveles de
prioridad.

Prioridad baja

psutil.BELOW_NORMAL_PRIORITY_CLASS

Prioridad alta

psutil.HIGH_PRIORITY_CLASS

El programa ejecuta el mismo cálculo matemático en ambos casos:

for i in range(10_000_000):
    resultado += math.sqrt(i)

El tiempo de ejecución se mide mediante:

time.time()

Ejecución con prioridad baja

python prioridad_procesos.py baja

Ejecución con prioridad alta

python prioridad_procesos.py alta

Prueba simultánea

Se pueden abrir dos terminales en VS Code y ejecutar:

Terminal 1:

python prioridad_procesos.py baja

Terminal 2:

python prioridad_procesos.py alta

De esta manera se pueden observar dos procesos ejecutando la misma carga
de trabajo con diferentes prioridades.

Nota: Una prioridad más alta no garantiza que el proceso siempre
termine primero. El resultado depende de factores como el procesador,
número de núcleos, carga del sistema, otros procesos y comportamiento
del planificador.

📸 Evidencias --- Prioridad de Procesos

Captura 1 --- Código fuente

Insertar aquí la captura de prioridad_procesos.py.

Descripción: Código utilizado para establecer las prioridades de los
procesos.

CAPTURA AQUÍ

Captura 2 --- Prioridad baja

Insertar aquí la captura de la ejecución con prioridad baja.

Descripción: Resultado y tiempo de ejecución del proceso con
prioridad BELOW_NORMAL.

CAPTURA AQUÍ

Captura 3 --- Prioridad alta

Insertar aquí la captura de la ejecución con prioridad alta.

Descripción: Resultado y tiempo de ejecución del proceso con
prioridad HIGH.

CAPTURA AQUÍ

Captura 4 --- Procesos ejecutándose simultáneamente

Insertar aquí la captura de las dos terminales ejecutando los
procesos.

Descripción: Comparación de dos instancias del programa con
diferentes niveles de prioridad.

CAPTURA AQUÍ

📊 Resumen de las prácticas

Programa                  Concepto principal      Herramientas

vigilante_recursos.py   Gestión de CPU y RAM    psutil, datetime,
time

simulador_cache.py      Caché y acceso a datos  dict, time

estres_memoria.py       Memoria virtual y       psutil, listas,
gestión de RAM          time

🧪 Resultados y observaciones

Vigilante de Recursos

Resultado obtenido:

Escribir aquí los resultados observados durante la ejecución.

Observaciones:

Escribir aquí las observaciones sobre CPU, RAM y generación del
archivo de alertas.

Simulador de Caché

Tiempo de primera lectura:

_____ segundos

Tiempo de lectura desde caché:

_____ segundos

Observación:

Escribir aquí la diferencia observada entre CACHE MISS y
CACHE HIT.

Estrés de Memoria

Límite configurado:

1000 MB

Comportamiento observado:

Escribir aquí qué ocurrió con el consumo de RAM durante la prueba.

Prioridad de Procesos

Tiempo con prioridad baja:

_____ segundos

Tiempo con prioridad alta:

_____ segundos

Observación:

Escribir aquí el comportamiento observado durante la ejecución
simultánea.

🎓 Conclusión

El desarrollo de estas prácticas permitió experimentar de manera directa
con diferentes funciones relacionadas con la administración de recursos
de un sistema operativo.

El primer ejercicio permitió monitorear el consumo de CPU y RAM y
generar registros de alerta. El segundo permitió comprender el principio
de una caché mediante el almacenamiento temporal de información en
memoria. El tercero permitió observar el comportamiento del consumo de
memoria mediante una asignación controlada y comprender el concepto de
memoria virtual. Finalmente, el cuarto ejercicio permitió experimentar
con la prioridad de procesos y comprender que el sistema operativo
utiliza mecanismos de planificación para administrar el uso de la CPU.

En conjunto, las prácticas permiten relacionar conceptos teóricos de
Sistemas Operativos con implementaciones prácticas desarrolladas en
Python.

👩‍💻 Autora

Nombre: Helen Alejandra Moncayo

Programa: Ingeniería de Software

Proyecto: Sistemas Operativos

