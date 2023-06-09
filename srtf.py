def srtfAlgo(procesos):
    n = len(procesos)
    tiempo_actual = 0
    procesos_completados = 0
    tiempo_espera_total = 0
    
    print('Ejecución de procesos: ')
    while procesos_completados < n:
        tiempo_mas_corto = float('inf')
        indice_mas_corto = -1

        # Encontrar el proceso con el tiempo restante mas corto
        for i in range(n):
            if procesos[i].tiempo_llegada <= tiempo_actual and procesos[i].tiempo_restante < tiempo_mas_corto and procesos[i].tiempo_restante > 0:
                tiempo_mas_corto = procesos[i].tiempo_restante
                indice_mas_corto = i

            
        if indice_mas_corto == -1:
            tiempo_actual += 1
            continue
        
        # Ejecutar el proceso por 1 unidad de tiempo
        procesos[indice_mas_corto].tiempo_restante -= 1
        tiempo_actual += 1

        print(f"Tiempo: {tiempo_actual - 1} - Proceso {procesos[indice_mas_corto].nombre} en ejecución")
    
        if procesos[indice_mas_corto].tiempo_restante == 0:
            procesos_completados += 1
            tiempo_retorno = tiempo_actual - procesos[indice_mas_corto].tiempo_llegada
            tiempo_espera = tiempo_retorno - procesos[indice_mas_corto].tiempo_rafaga
            tiempo_espera_total += tiempo_espera

            print(f"Proceso {procesos[indice_mas_corto].nombre}: Tiempo de retorno = {tiempo_retorno}, Tiempo de espera = {tiempo_espera}")
            tiempo_espera_promedio = tiempo_espera_total / n
            print(f"\nTiempo promedio de espera = {tiempo_espera_promedio}")
    

