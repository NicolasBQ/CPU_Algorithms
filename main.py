import fcfs

print('Ingrese el numero de procesos')
n = int(input())

processes = [] 

for i in range(n):
    process = {}
    print('Ingrese el nombre del proceso ', i + 1)
    processName = input()
    print('Ingrese el tiempo de llegada del proceso ', processName)
    ti = int(input())
    print('Ingrese el tiempo requerido para el proceso ', processName)
    tr = int(input())

    process['name'] = processName
    process['ti'] = ti
    process['tr'] = tr

    processes.append(process)

fcfs.fifoAlgo(processes, n)