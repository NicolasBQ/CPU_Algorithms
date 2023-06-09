import fcfs
import roundRobin
import spn
import srtf

cont = True

while cont:
    print("---- Seleccione que algoritmo quisiera ejectutar ----")
    print("1 - FCFS (First Come, First Serve)")
    print("2 - Round Robin")
    print("3 - SPN (Shortest Process Next)")
    print("4 - SRTF (Shortest Remaining Time First)")
    option = int(input())

    if option == 1:
        fcfs.fifoAlgo()
    elif option == 2:
        roundRobin.roundAlgo()
    elif option == 3:
        A = [
            {'id': 1, 'time': 5},
            {'id': 2, 'time': 1},
            {'id': 3, 'time': 11},
            {'id': 4, 'time': 9},
            {'id': 5, 'time': 3}
        ]
        print(spn.spnAlgo(A))
    elif option == 4:
        class Proceso:
            def __init__(self, nombre, tiempo_llegada, tiempo_proceso):
                self.nombre = nombre
                self.tiempo_llegada = tiempo_llegada
                self.tiempo_rafaga = tiempo_proceso
                self.tiempo_restante = tiempo_proceso

        proceso = [
            Proceso('P1,', 0, 2),
            Proceso('P2', 1, 1),
            Proceso('P3', 2, 3),
            Proceso('P4', 3, 2 ),
        ]
        srtf.srtfAlgo(proceso)
    else:
        print("Opción no registrada")

    print("---- Desea Continuar ----")
    print("1 - Continuar")
    print("2 - Salir")
    menuOption = int(input())

    if menuOption != 1:
        cont = False