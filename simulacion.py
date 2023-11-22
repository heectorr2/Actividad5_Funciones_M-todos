from datetime import datetime
"""
Actividad 1 - 25 puntos
Por consola se piden como máximo 5 números hasta que pulsas q
muestra la suma de los números introducidos.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
"""

def obtener_numero():
    while True:
        try:
            entrada = input("Introduce un número (o 'q' para salir): ")
            if entrada.lower() == 'q':
                return None
            else:
                return float(entrada)
        except ValueError:
            print("Error: Por favor, introduce un número válido.")
def suma():
    numero = obtener_numero()
    if numero is None:
        return 0
    else:
        return numero + suma()
def solucion():
    print("Introduce hasta 5 números. Para terminar, ingresa 'q'.")
    try:
        resultado = suma()
        print(f"La suma de los números introducidos es: {resultado}")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")

"""
Actividad 2
En consola se piden las unidades y el precio.
Estos datos permiten calcular el subtotal.
Si el día de hoy es anterior al 15 de cada mes, se aplica
un descuento del 5%
Muestra el resultado el total de la factura.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
"""

obtener_valor = lambda etiqueta: int(input(f"Ingrese {etiqueta}: "))
def calcular_subtotal(unidades, precio):
    return unidades * precio
def aplicar_descuento(subtotal):
    hoy = datetime.now()
    dia_del_mes = hoy.day
    descuento_func = lambda x: x * 0.95 if dia_del_mes < 15 else x
    return descuento_func(subtotal)
def solucion2():
    unidades = obtener_valor("unidades")
    precio = obtener_valor("precio por unidad")

    subtotal = calcular_subtotal(unidades, precio)
    total = aplicar_descuento(subtotal)

    print(f"Subtotal: {subtotal:.2f}€")
    print(f"Total con descuento: {total:.2f}€")

"""
Actividad 3
En consola pides número inicial.
En consola pides número final.
Muestra una lista con todos los números pares que hay entre 
estos dos números.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
"""

def obtener_numero_inicial():
    while True:
        try:
            numero_inicial = int(input("Ingrese el número inicial: "))
            return numero_inicial
        except ValueError:
            print("Error: Ingrese un número entero válido.")
def obtener_numero_final():
    while True:
        try:
            numero_final = int(input("Ingrese el número final: "))
            return numero_final
        except ValueError:
            print("Error: Ingrese un número entero válido.")
def generar_lista_pares(inicial, final):
    return [numero for numero in range(inicial, final + 1) if numero % 2 == 0]
def solucion3():
    try:
        numero_inicial = obtener_numero_inicial()
        numero_final = obtener_numero_final()

        if numero_inicial > numero_final:
            print("Error: El número inicial debe ser menor o igual al número final.")
            return

        lista_pares = generar_lista_pares(numero_inicial, numero_final)

        if not lista_pares:
            print(f"No hay números pares entre {numero_inicial} y {numero_final}.")
        else:
            print(f"Números pares entre {numero_inicial} y {numero_final}:")
            print(lista_pares)

    except Exception as e:
        print(f"Error inesperado: {e}")
