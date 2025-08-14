# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
import random 


Ventana_principal = Tk()
    
def salir():
    messagebox.showinfo("Suma 1.0","La app se cerrará")
    Ventana_principal.destroy()
 

#Titulo de la ventana

Ventana_principal.title("Jorge Luis Silva Morales")

#tamaño de la ventana
Ventana_principal.geometry("800x500")

#Deshabilitar el botón de maximizar de la ventana
Ventana_principal.resizable(0,0)

#color de fondo de la ventana

Ventana_principal.config(bg="black")

#frames

#frame 1 (maquina)
frame_1 = Frame(Ventana_principal)
frame_1.config(bg="ivory2",width=780, height=200)
frame_1.place(x=10,y=10)

#frame 2 (jugador)
frame_2 = Frame(Ventana_principal)
frame_2.config(bg="ivory2",width=780, height=125)
frame_2.place(x=10,y=230)

#frame 3, resutado, reintento y cierre
frame_3 = Frame(Ventana_principal)
frame_3.config(bg="ivory2",width=780, height=125)
frame_3.place(x=10,y=370)

titulo = Label(frame_1, text="¡Piedra Papel o Tijeras!")
titulo.config(bg="gray", fg="white", font=("Arial", 18))
titulo.place(x=260, y=10)

subtitulo1= Label(frame_1, text= "¡Juega contra la computadora!")
subtitulo1.config(bg="gray",fg="white", font=("Arial",12))
subtitulo1.place(x=270,y=43)

#logo

logo=PhotoImage(file="/home/sistemas/Documentos/Ejercicios_tkinter/piedra-papel-tijera_tkinter/Img/logodeljuego (1).png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=330,y=80)


#   botones
img_bt_papel= PhotoImage(file="/home/sistemas/Documentos/Ejercicios_tkinter/piedra-papel-tijera_tkinter/Img/papel.png")
bt_papel=Button(frame_2,image=img_bt_papel, width=105,height=105)
bt_papel.place(x=130,y=7)

img_bt_piedra= PhotoImage(file="/home/sistemas/Documentos/Ejercicios_tkinter/piedra-papel-tijera_tkinter/Img/piedra.png")
bt_piedra=Button(frame_2,image=img_bt_piedra, width=105,height=105)
bt_piedra.place(x=330,y=7)

img_bt_tijera= PhotoImage(file="/home/sistemas/Documentos/Ejercicios_tkinter/piedra-papel-tijera_tkinter/Img/images.png")
bt_tijera=Button(frame_2,image=img_bt_tijera, width=105,height=105)
bt_tijera.place(x=530,y=7)

#boton salir
img_bt_salir= PhotoImage(file="/home/sistemas/Documentos/Ejercicios_tkinter/piedra-papel-tijera_tkinter/Img/boton_salir.png")
bt_salir=Button(frame_3,image=img_bt_salir, width=105,height=105,command=salir)
bt_salir.place(x=530,y=7)  






#Codigo del piedra papel o tijera mezclado con la interfaz:



Ventana_principal.mainloop()
