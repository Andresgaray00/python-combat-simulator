import random



def generar_daño(minimo, maximo):
    return random.randint(minimo, maximo)


def mostrar_estado(nombre_h, hp_h, nombre_e, hp_e):
    print("\n--- ESTADO ACTUAL ---")
    print(f"{nombre_h}: {hp_h} HP")
    print(f"{nombre_e}: {hp_e} HP")
    print("---------------------\n")


def turno_jugador(hp_enemigo, hp_heroe, pociones):
    print("Elige una acción:")
    print("1. Atacar")
    print("2. Curar")
    print("3. Habilidad Especial")

    opcion = input("Opción: ")

    if opcion == "1":
        daño = generar_daño(10, 25)
        hp_enemigo -= daño
        print(f"¡Atacaste e hiciste {daño} de daño!")

    elif opcion == "2":
        if pociones > 0:
            hp_heroe += 20
            pociones -= 1
            print("Te curaste 20 HP.")
        else:
            print("¡No tienes pociones!")
    
    elif opcion == "3":
        probabilidad = random.randint(1, 2)
        if probabilidad == 1:
            daño = generar_daño(30, 50)
            hp_enemigo -= daño
            print(f"¡Habilidad especial! Hiciste {daño} de daño.")
        else:
            print("¡Fallaste la habilidad especial!")

    else:
        print("Opción inválida.")

    return hp_enemigo, hp_heroe, pociones


def turno_enemigo(hp_heroe):
    daño = generar_daño(15, 20)
    hp_heroe -= daño
    print(f"El enemigo te atacó e hizo {daño} de daño.")
    return hp_heroe


def verificar_ganador(hp_h, hp_e):
    if hp_h <= 0:
        print(" Has perdido")
        return True
    elif hp_e <= 0:
        print(" ¡Ganaste el combate!")
        return True
    return False
