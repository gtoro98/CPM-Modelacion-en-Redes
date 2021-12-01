from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import colorchooser
from time import *
from tkinter import font


def create_new_window(main_window):
    new_window = Tk()

def close_window(main_window):
    main_window.destroy()

def write_string_on_temp(string):
    f = open("temp.txt","w+")
    f.write(string)
    f.close()

def new_activity():

    pass

def new_window():
    window1 = Tk()
    window1.title("Agregar actividades")
    window1.geometry("800x400")

    message0 = Label(window1, 
                    text="Indique un identificador para la actividad:", 
                    font=("Arial",14,"bold"),
                    justify="center",
                    ).place(x=250,y=20)

    message1 = Label(window1, 
                    text="Indique un identificador para la actividad:", 
                    font=("Arial",10,),
                    justify="right",
                    ).place(x=20,y=80)
    
    id = Entry(window1, width= 15)
    id.place(x=270,y=80)

    message2 = Label(window1, 
                    text="Ingrese una descripción para la actividad:", 
                    font=("Arial",10,),
                    justify="right",
                    ).place(x=20,y=110)

    description = Entry(window1, width= 15)
    description.place(x=270,y=110)

    message3 = Label(window1, 
                    text="Ingrese la duración de la actividad:", 
                    font=("Arial",10,),
                    justify="right",
                    ).place(x=20,y=140)
    duration = Entry(window1, width= 15)
    duration.place(x=270,y=140)

    combo_box = ttk.Combobox(window1, width =10, font=font.Font(size=10))
    combo_box["state"] = "readonly"
    combo_box.place(x= 370, y= 138)
    combo_box["values"] = ("","Días","Semanas","Meses")
    combo_box.current(0)

    string = ""

    add = Button(window1, text="Agregar actividad", font=font.Font(size=9), command= lambda: write_string_on_temp(string)).place(x=350, y=350)
    

def add_activities(spinner_activities):
    number_of_activities = spinner_activities.get()
    counter = 0
    new_window()
    while counter < int(number_of_activities):
        
        counter = counter + 1


def main_window_function():
  
    def update_time():
        time = strftime("Hora: " + "%I:%M:%S %p")
        time_label.config(text=time, background="light grey")
        time_label.after(1000,update_time)
        day = strftime("%A")
        day_label.config(text=day, background="light grey", )

    #CREAR PANTALLA Y DETALLES DE LA MISMA #########################################################################################
    main_window = Tk()
    frame = Frame(main_window).place(x = 0, y = 0)
    main_window.geometry("800x600")
    main_window.title("CPM - Ruta Crítica")
    main_window.config(background="light grey")

    #icon = PhotoImage(file="logo.png")
    #main_window.iconphoto(True, icon)

    #HORA Y FECHA CONFIGURACION #####################################################################################################
    time_label = Label(frame, font=("Arial",10), # tiempo
                        background = "light grey",
                        justify= "right")
    time_label.place(x=680,y=0)

    day_label = Label(frame, font=("Arial",10), 
                        background = "light grey",
                        justify = "right")
    day_label.place(x=703, y=20)

    update_time()

    #BOTONES ##############################################################################################################

    add_activity = Button(frame, text="Agregar actividades", font=font.Font(size=10), command= lambda: add_activities(spinner_activities)).place(x=350, y=550)


    #LABEL TITULO ##########################################################################################################
    labelTitulo = Label(frame,  #titulo
                    text="CPM - Ruta crítica.", 
                    background="light grey", 
                    font=("Arial",16,"bold"),
                    justify="center",
                    )
    labelTitulo.place(x = 300, y = 60)

    #LABEL MENSAJEs ##########################################################################################################

    message1 = Label(frame,  
                    text="El método de la ruta crítica o diagrama CPM (Critical Path Method) por sus siglas en inglés\n es un algoritmo basado en la teoría de redes que permite calcular el tiempo mínimo de realización de un proyecto.", 
                    background="light grey", 
                    font=("Arial", 10),
                    justify="center",
                    )

    message1.place(x= 70,y=100)

    message2 = Label(frame,  
                    text="Esta herramienta permitirá organizar tus proyectos de manera eficiente", 
                    background="light grey", 
                    font=("Arial", 10),
                    justify="center",
                    )

    message2.place(x=70,y=200)

    message3 = Label(frame,  
                    text="Para comenzar, por favor indica en número de actividades que componen el proyecto: ", 
                    background="light grey", 
                    font=("Arial", 10),
                    justify="center",
                    )

    message3.place(x=70,y=250)

    #LABEL TIEMPO INFO #####################################################################################################

    spinner_activities = ttk.Spinbox(from_=0, to=10000, increment=1, state="readonly")  ## *****************quitar el readonly
    spinner_activities.place(x=600, y=250, width=50)



    #LABEL TIEMPO INFO #####################################################################################################
    labelTiempo = Label(frame,text="",
                        background="light grey", 
                        font=("Arial",18,"bold italic"),
                        justify="center",)
    labelTiempo.place(x=140,y=340) 





    main_window.mainloop()

main_window_function()