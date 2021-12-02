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


        #agregamos sus sucesores a la cola
        #print(tabla_sucesor)
        #sucesores = []
        sucesores = list(filter(lambda x: x['numero_act'] == nodo['numero_act'], tabla_sucesor))
        print("Sucesores: " + str(sucesores))

        #for sucesor in sucesores:
            #cola.append(sucesor)
        
    return