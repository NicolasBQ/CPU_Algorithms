from tabulate import tabulate

def fifoAlgo(processes, n):
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

        process['name'].append(name)
        process['init'].append(init)
        process['end'].append(end)
        process['T'].append(T)
        process['E'].append(E)
        process['P'].append(P)

    Taverage = Tsum / n
    Eaverage = Esum / n
    Paverage = Psum / n
    print(tabulate(process, headers='keys', tablefmt='fancy_grid'))
    print('Promedio T: ', Taverage)
    print('Promedio E; ', Eaverage)
    print('Promedio P: ', Paverage)
    


