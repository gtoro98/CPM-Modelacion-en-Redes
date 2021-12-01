def cpm(actividades):

    tabla_cpm = crear_tabla_cpm(actividades)
    tabla_sucesor = crear_tabla_sucesor(actividades)

    tabla_cpm = forward(tabla_cpm, tabla_sucesor, actividades)
    
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
    print(tabla_sucesor)    
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
        sucesores = list(filter(lambda x: x['numero_act'] == nodo['numero_act'], tabla_sucesor))
        print("Sucesores: " + str(sucesores))

        #agregamos los sucesores a la cola
        for sucesor in sucesores:
            cola.append(next(actividad for actividad in actividades if actividad["numero_act"] == sucesor['sucesor']))

        ES = 0
        EF = 0
        #Calculamos el ES buscando el maximo EF de los predecesores
        if len(nodo['predecesor']) > 0:
            for pred in nodo['predecesor']:
                if tabla_cpm[pred]['EF'] > ES:
                    ES = tabla_cpm[pred]['EF']

        tabla_cpm[nodo['numero_act']]['ES'] = ES
    
        #Calculamos el EF sumando la duracion al ES
        tabla_cpm[nodo['numero_act']]['EF'] = ES + tabla_cpm[nodo['numero_act']]['duracion']

    print(tabla_cpm)
    tabla_cpm = backward(tabla_cpm, actividades, tabla_sucesor)
    return tabla_cpm

def backward(tabla_cpm, actividades, tabla_sucesor):

    cola = []

    #calculamos la duracion total del proyecto
    duracion_proyecto = max(tabla_cpm, key=lambda x:x['EF'])['EF']

    #agregamos las actividades finales a la cola
    for actividad in tabla_cpm:
        if len(list(filter(lambda x: x['numero_act'] == actividad['numero_act'], tabla_sucesor))) == 0:
            cola.append(actividad)
    #actividad_final = list(filter(lambda x: x['EF'] == duracion_proyecto, tabla_cpm))
    #print("Actividad Final: " + str(actividad_final))
    #cola = actividad_final

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

    print("Las actividades en la ruta critica son: " + str(ruta_critica))
    return