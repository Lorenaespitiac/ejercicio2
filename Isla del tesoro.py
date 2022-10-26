print("Bienvenidos a la Isla, tu mision será encontrar el tesoro")
selva= input("entrarias a la selva o sigues a la playa? (playa o selva)")
if selva=="playa":
    print("No sabia nadar y no tenia bote, se ahogo! Game Over")
    exit(0)
elif selva=="selva":
    necesario= input("tienes todo lo necesario para entrar a la selva? (si o no)")
    if necesario=="no":
        print("Fue atacado por insectos y no tenia repelente. Game Over")
        exit(0)
    elif necesario=="si":
        print("Entra a la selva")
        camino= input("tienes dos caminos, derecha o izquierda")
        if camino=="derecha":
            print("Cae en arena movediza. Game Over")
            exit(0)
        elif camino=="izquierda":
            print("Llega a una Cueva")
            print("Hay una caja misteriosa y la abre")
            print("Esta el mapa pero debes realizar un acertijo para obtenerlo")
            acertijo= input("Estoy en todo pese a estar en nada, que soy?")
            if acertijo!="d":
                print("Fin de los intentos. Game Over")
                exit(0)
            elif acertijo=="d":
                print("Obtienes el mapa")
                print("Sigues el Camino indicado en el Mapa")
                print("Conseguiste el Tesoro")
                print("Ganaste!!")