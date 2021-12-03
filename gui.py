from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import *
from tkinter import font
from camino_critico import*
from grafo import*

f = open("temp.txt","w+")

def close_new_window(new_window):
    new_window.destroy()

def close_window(main_window):
    main_window.destroy()

def read():
    f = open("temp.txt","r")
    string = ""
    string = f.readline()
    f.close()
    return string

def write_string_on_temp(num_act, description, duration,predecesor_field, window1, counter):
    string = read()
    
    if predecesor_field.get() == "":
        predecesor = ""    
    else:
        predecesor = predecesor_field.get()

    string1 = string + num_act.get() + "-" + description.get() + "-" + duration.get() + "-" + predecesor + ";"
    counter = counter + 1

    print("Actividad "+ num_act.get() +":  Descripción: "+ description.get() +"  Duración: "+str(duration.get())+"  Predecesor: "+str(predecesor))

    f = open("temp.txt","w+")
    f.write(string1)
    f.close()
    window1.destroy()

    desition = messagebox.askyesno(message="¿Desea agregar otra actividad?")
    if desition == True:
        activity(counter)
    else:
        messagebox.showinfo(message="Se han agregado las actividades de forma satisfactoria.")

#VENTANA AGREGAR ACTIVIDADES ##############################################################################################################
def activity(counter): 

    window1 = Tk()
    frame = Frame(window1).place(x = 0, y = 0)
    window1.title("Agregar actividades")
    window1.geometry("800x400")
    window1.config(background="#FAB382")

    message0 = Label(window1, 
                    text="INGRESE LOS DATOS DE LA ACTIVIDAD", 
                    background="#FAB382", 
                    font=("Arial",18,"bold"),
                    justify="center",
                    ).place(x=150,y=20)
    
    message1 = Label(window1, 
                    text="Ingrese el número de la actividad:",
                    background="#FAB382",  
                    font=("Arial",14,),
                    justify="center",
                    ).place(x=150,y=90)

    num_act = Entry(window1, width= 15, font=font.Font(size=12))
    num_act.place(x=475,y=90)

    message2 = Label(window1, 
                    text="Ingrese un nombre para la actividad:",
                    background="#FAB382",  
                    font=("Arial",14,),
                    justify="center",
                    ).place(x=150,y=130)

    description = Entry(window1, width= 15, font=font.Font(size=12))
    description.place(x=475,y=130)

    message3 = Label(window1, 
                    text="Ingrese la duración de la actividad:", 
                    background="#FAB382", 
                    font=("Arial",14,),
                    justify="right",
                    ).place(x=150,y=170)

    duration = Entry(window1, width= 15, font=font.Font(size=12))
    duration.place(x=475,y=170)

    message4 = Label(window1, 
                    text="Ingrese los predecesor usando ( , ): ", 
                    background="#FAB382", 
                    font=("Arial",14,),
                    justify="right",
                    ).place(x=150,y=210)

    predecesor_field = Entry(window1, width= 15, font=font.Font(size=12))
    predecesor_field.place(x= 475, y= 210)
                                                                                        
    add = Button(window1, text="Agregar Actividad", command= lambda: write_string_on_temp(num_act, description, duration, predecesor_field, window1, counter),  width =20, bg='#FF5733', fg='#ffffff', font=font.Font(size=22, weight='bold')).place(x=300, y=280)
             

def main_window_function():
    actividades = []
    counter = 0
    
    def get_critical_route():
        string = read()
        a = string.split(";") #['0-Cemento-2-', '1-Mufa-2-2,1', '']
        actividades.clear()

        for i in range(0,len(a)-1): #0,1
            if "," in a[i].split("-")[3]: # Picas a en 4 pedazos. ['0', 'cemento','2',""]  ['1','mufa','2','2,1'] array de 0-3 posiciones
                predecesors = list(map(int, a[i].split("-")[3].split(",")))
            else:
                predecesors = list(map(int, a[i].split("-")[3]))
            actividades.append({"numero_act": int(a[i].split("-")[0]), "descripcion": a[i].split("-")[1], "duracion": int(a[i].split("-")[2]),"predecesor": predecesors})

        actividades_odenadas = sorted(actividades, key=lambda x: x["numero_act"])
        actividades.clear()
        for act_ord in actividades_odenadas:
            actividades.append(act_ord)
            
        print("\n|------Actividades Ingresadas------|")
        for acti in actividades:
            print(acti)

        CPM=cpm(actividades)

        RC = calcular_camino_critico(CPM)
        label_rutaCritica= "Las actividades en la ruta critica son:\n["+str(RC[0])+"]"
        for i in range(len(RC)-1):
            label_rutaCritica = label_rutaCritica + "➜["+str(RC[i+1])+"]"
        labelRutaCritica.config(text=label_rutaCritica, background="light green") #se llena el label con el tiempo

        crearGrafo(CPM, actividades,RC)

    def update_time():
        time = strftime("Hora: " + "%I:%M:%S %p")
        time_label.config(text=time, background="light blue")
        time_label.after(1000,update_time)
        day = strftime("%A")
        day_label.config(text=day, background="light blue", )

    #ABRIR VENTANA CON ACTIVIDADES ###############################################################################  
    def openNewWindowActividades():
        newWindow = Toplevel(main_window)
        newWindow.title("Lista de Actividades:")
        newWindow.geometry("700x700")
        newWindow.config(background="#DB6060")

        label_verAct=""
        for i in range(len(actividades)):
            label_verAct =label_verAct+str(actividades[i])+"\n"

        label_verAct = Label(newWindow,  
                    text=label_verAct, 
                    background="#DB6060", 
                    font=("Arial",12,"bold"),
                    justify="left",
                    )
        label_verAct.place(x=0, y=0)
    
    #ABRIR VENTANA CON TABLA CPM ###############################################################################  
    def openNewWindowTablaCPM():
        newWindow = Toplevel(main_window)
        newWindow.title("Tabla CPM:")
        newWindow.geometry("800x700")
        newWindow.config(background="#A0C4F0")

        if(len(actividades)>0):
            label_verCPMtext=""
            tableCPM = cpm_gui(actividades)
            for i in range(len(tableCPM)):
                label_verCPMtext =label_verCPMtext+str(tableCPM[i])+"\n"

            label_verCPM = Label(newWindow,  
                        text=label_verCPMtext, 
                        background="#A0C4F0", 
                        font=("Arial",12,"bold"),
                        justify="left",
                        )
            label_verCPM.place(x=0, y=0)

    #ABRIR MOSTRAR GRAFO ###############################################################################  
    def openNewWindowGrafo():
        if(len(actividades)>0):
            tabla_cpm=cpm_gui(actividades)
            RutaMasCorta=calcular_camino_critico(tabla_cpm)
            crearGrafo(tabla_cpm, actividades,RutaMasCorta)

    #CREAR PANTALLA Y DETALLES DE LA MISMA #########################################################################################
    main_window = Tk()
    frame = Frame(main_window).place(x = 0, y = 0)
    main_window.geometry("800x600")
    main_window.title("CPM - Ruta Crítica")
    main_window.config(background="light blue")


    #HORA Y FECHA CONFIGURACION #####################################################################################################
    time_label = Label(frame, font=("Arial",10), # tiempo
                        background = "light blue",
                        justify= "right")
    time_label.place(x=0,y=0)

    day_label = Label(frame, font=("Arial",10), 
                        background = "light blue",
                        justify = "right")
    day_label.place(x=0, y=20)

    update_time()

    #BOTONES ##############################################################################################################
    close_button = Button(frame, text="X", font=font.Font(size=15, weight='bold'), width=3, command= lambda: close_window(main_window), bg='red').pack(side=TOP, anchor=E)

    add_activity_button = Button(main_window, text="Agregar actividades", command= lambda: activity(counter), width =16, bg='#FF5733', fg='#ffffff', font=font.Font(size=13, weight='bold')).place(x=290, y=180)

    critical_route_button = Button(main_window, text=" Hallar CPM", command= get_critical_route, width =16, bg='#900C3F', fg='#ffffff', font=font.Font(size=13, weight='bold')).place(x=290, y=220)

    verActividades_button = Button(main_window, text="Ver Actividades", command=openNewWindowActividades, width =13, bg='#C70039', fg='#ffffff', font=font.Font(size=14, weight='bold')).place(x = 80, y = 500) 

    verTablaCPM_button = Button(main_window, text="Tabla CPM",  command=openNewWindowTablaCPM, width =13, bg='#0052cc', fg='#ffffff', font=font.Font(size=14, weight='bold')).place(x = 300, y = 500)

    verGrafo_button = Button(main_window, text="Ver Grafo",  command=openNewWindowGrafo, width =13, bg='#FFC300', fg='#ffffff', font=font.Font(size=14, weight='bold')).place(x = 520, y = 500)

    #LABEL TITULO ##########################################################################################################
    labelTitulo = Label(frame,  #titulo
                    text="CPM - Critical Path Method", 
                    background="light blue", 
                    font=("Arial",18,"bold"),
                    justify="center",
                    )
    labelTitulo.place(x = 240, y = 60)

    #LABEL MENSAJEs ##########################################################################################################

    message1 = Label(frame,  
                    text="El método de la ruta crítica o diagrama CPM (Critical Path Method) por sus siglas en inglés\n es un algoritmo basado en la teoría de redes que permite calcular el tiempo mínimo de realización de un proyecto.", 
                    background="light blue", 
                    font=("Arial", 12),
                    justify="center",
                    )

    message1.place(x= 0,y=100)

    message2 = Label(frame,  
                    text="Para comenzar: \n\n1- Agrege Actividades:\n\n2- Halle su ruta critica:", 
                    background="light Blue", 
                    font=("Arial", 12, "bold"),
                    justify="left",
                    )

    message2.place(x=100,y=150)

    #LABEL TIEMPO INFO #####################################################################################################
    labelRutaCritica = Label(frame,text="",
                        background="light blue", 
                        font=("Arial",18,"bold italic"),
                        justify="center",)
    labelRutaCritica.place(x=100,y=340) 

    main_window.mainloop()

