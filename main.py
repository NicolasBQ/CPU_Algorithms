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
        spn.spnAlgo()
    elif option == 4:
        srtf.srtfAlgo()
    else:
        print("Opción no registrada")

    print("---- Desea Continuar ----")
    print("1 - Continuar")
    print("2 - Salir")
    menuOption = int(input())

    if menuOption != 1:
        cont = False