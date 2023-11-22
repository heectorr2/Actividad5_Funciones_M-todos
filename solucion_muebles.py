from muebles import Silla

def crear_sillas():
    try:
        silla_azul = Silla(color="azul", precio=9.95)
        silla_roja = Silla(color="roja", precio=9.95)

        print("Se han creado dos sillas:")
        print(f"Silla Azul - Color: {silla_azul.color}, Precio: ${silla_azul.precio:.2f}")
        print(f"Silla Roja - Color: {silla_roja.color}, Precio: ${silla_roja.precio:.2f}")

    except Exception as e:
        print(f"Error inesperado al crear las sillas: {e}")


crear_sillas()