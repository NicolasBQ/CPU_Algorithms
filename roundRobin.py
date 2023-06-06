from tabulate import tabulate

def roundAlgo():
    print('Ingrese el numero de procesos')
    n = int(input())
    print('Ingrese el valor de quantum (q)')
    q = int(input())
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

    order = sequence(processes, q)
    algo(processes, n, order)


def sequence(processes, q):
    length = len(processes)
    copyProcesses = []

    for j in processes:
        copy = j.copy()
        copyProcesses.append(copy)

    order = {}
    order['process'] = []
    order['time'] = []
    order['rest'] = []

    i = 0
    while i < length:
        if copyProcesses[i]['tr'] > q:
            order['process'].append(copyProcesses[i]['name'])
            order['time'].append(q)
            copyProcesses[i]['tr'] = copyProcesses[i]['tr'] - q
            copyProcesses.insert(i + 2, copyProcesses[i])
            order['rest'].append(copyProcesses[i]['tr'])
            length = len(copyProcesses)
            i += 1
        else:
            order['process'].append(copyProcesses[i]['name'])
            order['time'].append(copyProcesses[i]['tr'])
            order['rest'].append(copyProcesses[i]['tr'] - copyProcesses[i]['tr'])
            i += 1
    print(tabulate(order, headers='keys', tablefmt='fancy_grid'))
    return order

def algo(processes, n, order): 
    process = {}
    process['name'] = []
    process['init'] = []
    process['end'] = []
    process['T'] = []
    process['E'] = []
    process['P'] = []

    totalLength = len(order['process'])
    initialIndexes = []
    for j in range(n):
        process['name'].append(processes[j]['name'])
        for k in range(totalLength):
            if processes[j]['name'] == order['process'][k]:
                initialIndexes.append(k)
                break
    
    finalIndexes = []
    for x in range(n):
        for z in range(totalLength):
            if processes[x]['name'] == order['process'][z]:
                currentIndex = z
        finalIndexes.append(currentIndex)


    for c in range(n):
        i = 0
        init = 0
        while i < initialIndexes[c]:
            init += order['time'][i]
            i += 1
        process['init'].append(init)
    
    for b in range(n):
        i = 0
        end = 0
        while i <= finalIndexes[b]:
            end += order['time'][i]
            i += 1 

        T = end - processes[b]['ti']
        E = T - processes[b]['tr']
        P = T / processes[b]['tr']

        process['end'].append(end)
        process['T'].append(T)
        process['E'].append(E)
        process['P'].append(P)
    

    
    print(tabulate(process, headers='keys', tablefmt='fancy_grid'))
