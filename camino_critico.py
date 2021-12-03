def cpm(actividades):
    #CREAR TABLA CPM E IMPRIMIRLA
    tabla_cpm = crear_tabla_cpm(actividades)
    print("\n|----------------Inicialización Tabla CPM---------------|")
    for cpm in tabla_cpm:
        print(cpm)

    #CREAR TABLA SUCESORES E IMPRIMIRLA
    tabla_sucesor = crear_tabla_sucesor(actividades)
    print("\n|-----------Inicialización Tabla De SUCESORES-----------|")     
    for suce in tabla_sucesor:
        print(suce)   

    #HACER FORWARD EN LA TABLA CPM E IMPRIMIRLA
    print("\nCORRIENDO FORWARD ...")
    tabla_cpm = forward(tabla_cpm, tabla_sucesor, actividades)
    print("\n|----------------Forward Tabla CPM---------------|")
    for cpm in tabla_cpm:
        print(cpm)

    #HACER BACKWARD EN LA TABLA CPM E IMPRIMIRLA
    tabla_cpm = backward(tabla_cpm, actividades, tabla_sucesor)
    print("\n|----------------Backward Tabla CPM---------------|")
    for cpm in tabla_cpm:
        print(cpm)

    return tabla_cpm

def crear_tabla_cpm(actividades):

    tabla_cpm = []

    for actividad in actividades:
        tabla_cpm.append({
            "actividad": actividad['descripcion'],
            "numero_act": actividad['numero_act'], 
            "duracion": actividad['duracion'], 
            "ES": None, 
            "EF": None, 
            "LS": None, 
            "LF": None, 
            "holgura": None})

    return tabla_cpm

def crear_tabla_sucesor(actividades):
    
    tabla_sucesor = []

    for actividad in actividades:
        sucesor = actividad['numero_act']

        for predecesor in actividad['predecesor']:
            tabla_sucesor.append({"numero_act": predecesor, "sucesor": sucesor})

    return tabla_sucesor

def forward(tabla_cpm, tabla_sucesor, actividades):

    cola = []
    #agregamos las actividades iniciales a la cola
    for actividad in actividades:
        if len(actividad['predecesor']) == 0:
            cola.append(actividad)
    
    #mientras queden actividades
    while len(cola) > 0:
        nodo = cola.pop(0)
        print("Evaluando el nodo: " + str(nodo))

        #buscamos cuales son sus sucesores
        print("-Buscando sus sucesores:")
        sucesores = list(filter(lambda x: x['numero_act'] == nodo['numero_act'], tabla_sucesor))
        print("-Sucesores: " + str(sucesores))

        #agregamos los sucesores a la cola
        for sucesor in sucesores:
            cola.append(next(actividad for actividad in actividades if actividad["numero_act"] == sucesor['sucesor']))

        ES = 0
        EF = 0
        #Calculamos el ES buscando el maximo EF de los predecesores
        print("-Calculando ES y EF ... \n")
        if len(nodo['predecesor']) > 0:
            for pred in nodo['predecesor']:
                if tabla_cpm[pred]['EF'] > ES:
                    ES = tabla_cpm[pred]['EF']

        tabla_cpm[nodo['numero_act']]['ES'] = ES
    
        #Calculamos el EF sumando la duracion al ES
        tabla_cpm[nodo['numero_act']]['EF'] = ES + tabla_cpm[nodo['numero_act']]['duracion']

    return tabla_cpm

def backward(tabla_cpm, actividades, tabla_sucesor):

    cola = []

    #calculamos la duracion total del proyecto
    duracion_proyecto = max(tabla_cpm, key=lambda x:x['EF'])['EF']

    #agregamos las actividades finales a la cola
    for actividad in tabla_cpm:
        if len(list(filter(lambda x: x['numero_act'] == actividad['numero_act'], tabla_sucesor))) == 0:
            cola.append(actividad)

    while len(cola) > 0:
        nodo = cola.pop(0)
        
        if len(list(filter(lambda x: x['numero_act'] == nodo['numero_act'], tabla_sucesor))) == 0:
            tabla_cpm[nodo['numero_act']]['LF'] = duracion_proyecto

        else:
            sucesor =  list(filter(lambda x: x['numero_act'] == nodo['numero_act'], tabla_sucesor))
            LF = duracion_proyecto
            
            for suc in sucesor:
                try:
                    if tabla_cpm[suc['sucesor']]['LS'] < LF:
                        LF = tabla_cpm[suc['sucesor']]['LS']
                except TypeError:
                    break
            
            tabla_cpm[nodo['numero_act']]['LF'] = LF

        tabla_cpm[nodo['numero_act']]['LS'] = tabla_cpm[nodo['numero_act']]['LF'] - tabla_cpm[nodo['numero_act']]['duracion']

        #agregamos los predecesores a la cola
        for predecesor in actividades[nodo['numero_act']]['predecesor']:
            cola.append(next(actividad for actividad in tabla_cpm if actividad["numero_act"] == predecesor))
    
    tabla_cpm = calcular_holgura(tabla_cpm)
    return tabla_cpm

def calcular_holgura(tabla_cpm):

    for actividad in tabla_cpm:
        actividad['holgura'] = actividad['LS'] - actividad['ES']
    return tabla_cpm

def calcular_camino_critico(tabla_cpm):

    ruta_critica = []

    for actividad in tabla_cpm:
        if actividad['holgura'] == 0:
            ruta_critica.append(actividad['actividad'])
    
    print("\nLas actividades en la ruta critica son: " + str(ruta_critica))
    return ruta_critica

def cpm_gui(actividades):
    tabla_cpm = crear_tabla_cpm(actividades)
    tabla_sucesor = crear_tabla_sucesor(actividades)
    tabla_cpm = forward(tabla_cpm, tabla_sucesor, actividades)
    tabla_cpm = backward(tabla_cpm, actividades, tabla_sucesor)

    return tabla_cpm
