# se importa la libreria tkinter con todas sus funciones
from tkinter import *

Ventana_principal = Tk()

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

titulo = Label(frame_1, text="¡Piedra Papel o tijeras!")
titulo.config(bg="gray", fg="white", font=("Arial", 18))
titulo.place(x=260, y=10)

subtitulo1= Label(frame_1, text= "¡Juega contra la computadora!")
subtitulo1.config(bg="gray",fg="white", font=("Arial",12))
subtitulo1.place(x=270,y=43)











Ventana_principal.mainloop()
