
"""
Actividad 4
Crea un módulo con las siguientes clases
Mesa
Silla
Lampara
las tres clases tiene como atributo color y precio.
En otro módulo importa únicamente la clase Silla y crea dos sillas. Una de color azul y otra roja con precios de 9.95

algoritmo funciona:5 puntos
algoritmo utiliza características de POO : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica enumeradores o similar para Color : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
"""

class Mesa:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

class Silla:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

class Lampara:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio