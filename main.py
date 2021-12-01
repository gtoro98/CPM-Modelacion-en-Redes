from camino_critico import *

actividades = []
cant_act = int(input("Ingrese la cantidad de aactividades que contiene el proyecto"))


for i in range(cant_act): #0-35 preparar estructura de datos auxiliar: matriz nodo distancia minima predecesor y visitado

    print("Porfavor ingrese los datos de la actividad numero " + str(i)  + ": ") 

    numero_act = i
    descripcion = input("Ingrese la descripcion de la actividad " + str(i) + ": ")
    duracion = input("Ingrese la duracion de la actividad " + str(i)  + ": ")

    while type(duracion) != int:
        try:
            duracion = int(duracion)
        except ValueError:
            duracion = input("La duracion debe ser un numero entero, vuelva a ingresar la duracion de la actividad " + str(i)  + ": ")

    predecesor = []
    aux = None

    try:
        aux = int(input("Ingrese el numero de las actividades que precedan a esta en caso de no existir, presionar ENTER"))

        while type(aux) == int:
            if any(x == aux for x in predecesor):
                print("La actividad " + str(aux) + " ya esta de predecesor")

            elif any(actividad['numero_act'] == aux for actividad in actividades):
                predecesor.append(aux)
            else:
                print("La actividad " + str(aux) + " no existe")
            try:
                aux = int(input("Ingrese el numero de otras actividades que precedan a esta en caso de no existir, presionar ENTER"))
            except ValueError:
                break
    except ValueError:
        pass
    actividades.append({"numero_act": numero_act, "descripcion": descripcion, "duracion": duracion,"predecesor": predecesor})

cpm(actividades)
    #print(actividades)
    

     