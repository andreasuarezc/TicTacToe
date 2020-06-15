def tablero(ticTacToe):    
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",(ticTacToe[1]),"  |  ",(ticTacToe[2]),"  |  ",(ticTacToe[3]),"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",(ticTacToe[4]),"  |  ",(ticTacToe[5]),"  |  ",(ticTacToe[6]),"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",(ticTacToe[7]),"  |  ",(ticTacToe[8]),"  |  ",(ticTacToe[9]),"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def valorAleatorio(ticTacToe):
    import random
    maquina=random.choice(list(ticTacToe.keys()))
    return maquina

def jugadaMaquina(ticTacToe):
    maquina=valorAleatorio(ticTacToe)
    elemento=ticTacToe[maquina]
    if elemento=="O" or elemento=="X":
        return jugadaMaquina(ticTacToe)
    else:
        nuevaPosicion = ticTacToe[maquina] = "X"
        print("La juagada de la maquina es: ")
        return nuevaPosicion

def jugadaUsuario(ticTacToe):
    print("Ahora es tu turno. ¿Cuál posición deseas tomar?")
    posicion=int(input("Ingresa un número del 1 al 9 de la casillas disponibles: "))
    nuevaPosicion = ticTacToe[posicion] = "O"
    return nuevaPosicion
    
def respuesta(ticTacToe):
    if ticTacToe[1]=="X" and ticTacToe[2]=="X" and ticTacToe[3]=="X":
        print("La maquina Gana!")
        tablero(ticTacToe)
        juego = 1
        return juego
    else:
        if ticTacToe[4]=="X" and ticTacToe[5]=="X" and ticTacToe[6]=="X":
            print("La maquina Gana!")
            tablero(ticTacToe)
            juego = 1
            return juego
        else:
            if ticTacToe[7]=="X" and ticTacToe[8]=="X" and ticTacToe[9]=="X":
                print("La maquina Gana!")
                tablero(ticTacToe)
                juego = 1
                return juego
            else:
                if ticTacToe[1]=="X" and ticTacToe[4]=="X" and ticTacToe[7]=="X":
                    print("La maquina Gana!")
                    tablero(ticTacToe)
                    juego = 1
                    return juego
                else:
                    if ticTacToe[2]=="X" and ticTacToe[5]=="X" and ticTacToe[8]=="X":
                        print("La maquina Gana!")
                        tablero(ticTacToe)
                        juego = 1
                        return juego
                    else:
                        if ticTacToe[3]=="X" and ticTacToe[6]=="X" and ticTacToe[9]=="X":
                            print("La maquina Gana!")
                            tablero(ticTacToe)
                            juego = 1
                            return juego
                        else:
                            if ticTacToe[1]=="X" and ticTacToe[5]=="X" and ticTacToe[9]=="X":
                                print("La maquina Gana!")
                                tablero(ticTacToe)
                                juego = 1
                                return juego
                            else:
                                if ticTacToe[3]=="X" and ticTacToe[5]=="X" and ticTacToe[7]=="X":
                                    print("La maquina Gana!")
                                    tablero(ticTacToe)
                                    juego = 1
                                    return juego
                                else:
                                    if ticTacToe[1]=="O" and ticTacToe[2]=="O" and ticTacToe[3]=="O":
                                        print("Tu Ganas!")
                                        tablero(ticTacToe)
                                        juego = 1
                                        return juego
                                    else:                                        
                                        if ticTacToe[7]=="O" and ticTacToe[8]=="O" and ticTacToe[9]=="O":
                                            print("Tu Ganas!")
                                            tablero(ticTacToe)
                                            juego = 1
                                            return juego
                                        else:
                                            if ticTacToe[1]=="O" and ticTacToe[4]=="O" and ticTacToe[7]=="O":
                                                print("Tu Ganas!")
                                                tablero(ticTacToe)
                                                juego = 1
                                                return juego
                                            else:
                                                if ticTacToe[3]=="O" and ticTacToe[6]=="X" and ticTacToe[9]=="O":
                                                    print("Tu Ganas!")
                                                    tablero(ticTacToe)
                                                    juego = 1
                                                    return juego
                                                else:
                                                    if type(ticTacToe[1])!= int and type(ticTacToe[2])!= int and type(ticTacToe[3])!= int and type(ticTacToe[4])!= int and type(ticTacToe[5])!= int and type(ticTacToe[6])!= int and type(ticTacToe[7])!= int and type(ticTacToe[8])!= int and type(ticTacToe[9])!= int:
                                                        print("El juego termina en empate")
                                                        tablero(ticTacToe)
                                                        juego=1
                                                        return juego
                                                    else:
                                                        print("El juego continua")
                                                        juego=0
                                                        return juego
