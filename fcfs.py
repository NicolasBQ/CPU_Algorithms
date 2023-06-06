from tabulate import tabulate

def fifoAlgo():
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

    algo(processes, n)


def algo(processes, n):
    Tsum = 0
    Esum = 0
    Psum = 0
    end = processes[0]['ti']

    process = {}
    process['name'] = []
    process['init'] = []
    process['end'] = []
    process['T'] = []
    process['E'] = []
    process['P'] = []

    order = {}
    order['process'] = []
    order['time'] = []
    order['rest'] = []

    for i in range(n):
        name = processes[i]['name']
        init = end
        end = init + processes[i]['tr']
        T = end - processes[i]['ti']
        E = T - processes[i]['tr']
        P = T / processes[i]['tr']

        Tsum += T
        Esum += E
        Psum += P

        order['process'].append(name)
        order['time'].append(processes[i]['tr'])
        order['rest'].append(0)

        process['name'].append(name)
        process['init'].append(init)
        process['end'].append(end)
        process['T'].append(T)
        process['E'].append(E)
        process['P'].append(P)

    Taverage = Tsum / n
    Eaverage = Esum / n
    Paverage = Psum / n
    print(tabulate(order, headers='keys', tablefmt='fancy_grid'))
    print(tabulate(process, headers='keys', tablefmt='fancy_grid'))
    print('Promedio T: ', Taverage)
    print('Promedio E; ', Eaverage)
    print('Promedio P: ', Paverage)



