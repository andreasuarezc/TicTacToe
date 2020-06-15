#Bloque Inicial
from LogicaTicTacToe import tablero
from LogicaTicTacToe import jugadaMaquina
from LogicaTicTacToe import jugadaUsuario
from LogicaTicTacToe import respuesta
from LogicaTicTacToe import valorAleatorio

ticTacToe={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
juego = 0
print("Vamos a jugar Tic Tac Toe")
tablero(ticTacToe)
eleccion=input("¿Quieres empezar? SI/NO: ")
if eleccion.upper() == "SI":
    print("La jugada de la maquina estará representada con una X")
    print("Tu jugada va estar representada con una O")
    print("La primer Jugada la hace la maquina")
    ticTacToe[5] = "X"
    tablero(ticTacToe)
    while juego==0:
        jugadaUsuario(ticTacToe)
        tablero(ticTacToe)
        juego=respuesta(ticTacToe)
        if juego==1:
            break
        else:
            jugadaMaquina(ticTacToe)
            tablero(ticTacToe)
            juego=respuesta(ticTacToe)
else:
    print("Es una lastima que no puedas jugar ahora.")
    print("Te esperamos en una próxima ocasión.")
    
    
        


        
