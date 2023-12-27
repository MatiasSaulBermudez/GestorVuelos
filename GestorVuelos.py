def agregar_vuelo(vuelos, numero_vuelo, destino, hora_salida):
    vuelos[numero_vuelo] = {
        "destino": destino,
        "hora_salida": hora_salida
    }
    print("El vuelo", numero_vuelo, "se ha agregado correctamente.")


def actualizar_hora_salida(vuelos, numero_vuelo, nueva_hora_salida):
    if numero_vuelo in vuelos:
        vuelos[numero_vuelo]["hora_salida"] = nueva_hora_salida
        print("La hora de salida del vuelo", numero_vuelo,
              "se ha actualizado correctamente.")
    else:
        print("El número de vuelo", numero_vuelo, "no existe en el sistema.")


def ver_vuelos(vuelos):
    if len(vuelos) > 0:
        print("Detalles de los vuelos actuales:")
        for numero_vuelo, detalles in vuelos.items():
            print("Número de vuelo:", numero_vuelo)
            print("Destino:", detalles["destino"])
            print("Hora de salida:", detalles["hora_salida"])
            print()
    else:
        print("No hay vuelos registrados en el sistema.")


# Código principal
vuelos = {}

agregar_vuelo(vuelos, "123", "Madrid", "17:15")
agregar_vuelo(vuelos, "456", "Londres", "10:30")
agregar_vuelo(vuelos, "789", "París", "14:45")

actualizar_hora_salida(vuelos, "123", "18:30")

ver_vuelos(vuelos)
