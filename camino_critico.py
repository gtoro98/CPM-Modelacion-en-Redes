def cpm(actividades):

    tabla_cpm = crear_tabla_cpm(actividades)
    tabla_sucesor = crear_tabla_sucesor(actividades)

    forward(tabla_cpm, tabla_sucesor, actividades)
    return

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
    return