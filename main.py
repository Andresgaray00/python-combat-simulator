import functions

def main():
    nombre_heroe = "Héroe"
    nombre_enemigo = "Enemigo"

    hp_heroe = 100
    hp_enemigo = 120
    pociones = 3

    print(" ¡Bienvenido a Terminal Souls! ")

    while True:
        functions.mostrar_estado(nombre_heroe, hp_heroe, nombre_enemigo, hp_enemigo)

        hp_enemigo, hp_heroe, pociones = functions.turno_jugador(
            hp_enemigo, hp_heroe, pociones
        )

        if functions.verificar_ganador(hp_heroe, hp_enemigo):
            break

        hp_heroe = functions.turno_enemigo(hp_heroe)

        if functions.verificar_ganador(hp_heroe, hp_enemigo):
            break



main()