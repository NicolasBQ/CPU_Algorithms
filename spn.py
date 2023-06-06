def spnAlgo(processes):
    # Distribuye los procesos por su tiempo
    processes = sorted(processes, key=lambda p: p['time'])

    current_time = 0
    waiting_time = 0

    # Organiza por tiempo
    for process in processes:
        #Actualizacion de Waiting Time
        waiting_time += current_time

        #Actualizacion del Current_time
        current_time += process['time']

    # Calcula en promedio de tiempo de espera
    avg_waiting_time = waiting_time / len(processes)

    return avg_waiting_time