from tkinter import *
from tkinter import messagebox 
from tkinter import simpledialog 

'''Dentro de esta funcion vamos a bloquear cada uno de los botones'''
def bloquear():
    for i in range(0,9):
        listaBotones[i].config(state="disabled")

''' Creamos una funcion para que cuando hagamos click en el boton iniciar se habiliten los botones '''        
def iniciarJ():
    for i in range(0, 9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(bg="#5068A8")
        listaBotones[i].config(text =" ")
        t[i] = "N"

    #Pedimos los nombres de los jugadores
    global nombreJugador1,nombreJugador2
    nombreJugador1 = simpledialog.askstring("Jugador","Escribe el nombre del Jugador 1: ")
    nombreJugador2 = simpledialog.askstring("Jugador","Escribe el nombre del Jugador 2: ")
    #le decimosal usuario que va a empezar el jugador 1
    nombreJugador1 = nombreJugador1.title()
    nombreJugador2 = nombreJugador2.title()
    turnoJugador.set("Es turno de: " + nombreJugador1)


def cambiar(num):
            global turno,nombreJugador1,nombreJugador2
            if t[num] == "N" and turno == 0:
                listaBotones[num].config(text = "X")
                listaBotones[num].config(bg="#85c4cb")
                t[num]="X"
                turno = 1
                turnoJugador.set("Turno: " + nombreJugador2)
                
            elif t[num] == "N" and turno == 1:
                
                listaBotones[num].config(text = "O")
                listaBotones[num].config(bg="#ffb923")
                t[num]="O"
                turno = 0
                turnoJugador.set("Turno: " + nombreJugador1)
            listaBotones[num].config(state ="disabled")
            verificar()


def verificar():
    if ( t[0] == "X" and t[1] == "X" and t[2] == "X") or (t[3] == "X" and t[4] == "X" and t[5] == "X") or (t[6] == "X" and t[7] == "X" and t[8] == "X") :
        #turnoJugador.set("")
        bloquear()
        messagebox.showinfo("Ganador","Ganaste: " + nombreJugador1)
    
    elif (t[0] == "X" and t[3] == "X" and t[6] == "X") or (t[1] == "X" and t[4] == "X" and t[7] == "X") or (t[2] == "X" and t[5] == "X" and t[8] == "X"):
        #turnoJugador.set("")
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste: " + nombreJugador1)

    elif (t[0] == "X" and t[4] == "X" and t[8] == "X")  or (t[2] == "X" and t[4] == "X" and t[6] == "X"):
        #turnoJugador.set("")
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste: " + nombreJugador1)

        
    elif ( t[0] == "O" and t[1] == "O" and t[2] == "O") or (t[3] == "O" and t[4] == "O" and t[5] == "O")or (t[6] == "O" and t[7] == "X" and t[8] == "O") :
        #turnoJugador.set("")
        bloquear()
        messagebox.showinfo("Ganador","Ganaste: " + nombreJugador2)
        
    elif (t[0] == "O" and t[3] == "O" and t[6] == "O") or (t[1] == "O" and t[4] == "O" and t[7] == "O") or (t[2] == "O" and t[5] == "O" and t[8] == "O"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste: " + nombreJugador2)
        #turnoJugador.set("")
        
    elif (t[0] == "O" and t[4] == "O" and t[8] == "O")  or (t[2] == "O" and t[4] == "O" and t[6] == "O"):
        #turnoJugador.set("")       
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste: " + nombreJugador2)

ventana = Tk()
ventana.geometry("400x500+200+20")
ventana.title("Juego del Gato")
ventana.iconbitmap("mi_logo.ico")
ventana.config(bg="#000")


turno = 0
nombreJugador1 =""
nombreJugador2 =""
listaBotones = [ ]
t =[ ]
turnoJugador = StringVar()

for i in range(0,9):
    t.append("N")
    
boton0 = Button(ventana, width=9, height=3 , command= lambda: cambiar(0))
listaBotones.append(boton0)
boton0.place(x=50, y= 50)

boton1 = Button(ventana, width=9, height=3, command=lambda: cambiar(1))
listaBotones.append(boton1)
boton1.place(x=150, y= 50)

boton2 = Button(ventana, width=9, height=3, command=lambda: cambiar(2))
listaBotones.append(boton2)
boton2.place(x=250, y= 50)

boton3 = Button(ventana, width=9, height=3, command=lambda: cambiar(3))
listaBotones.append(boton3)
boton3.place(x=50, y= 150)

boton4 = Button(ventana, width=9, height=3, command=lambda: cambiar(4))
listaBotones.append(boton4)
boton4.place(x=150, y= 150)

boton5 = Button(ventana, width=9, height=3, command=lambda: cambiar(5))
listaBotones.append(boton5)
boton5.place(x=250, y= 150)

boton6 = Button(ventana, width=9, height=3, command=lambda: cambiar(6))
listaBotones.append(boton6)
boton6.place(x=50, y= 250)

boton7 = Button(ventana, width=9, height=3 , command= lambda: cambiar(7))
listaBotones.append(boton7)
boton7.place(x=150, y= 250)

boton8 = Button(ventana, width=9, height=3, command=lambda: cambiar(8))
listaBotones.append(boton8)
boton8.place(x=250, y= 250)

#etiqueta para ver a que jugador le toca el turno
turnoE = Label(ventana, textvariable=turnoJugador, font=(
    "Arial Rounded MT Bold", 15), fg="#fff", bg="#000").place(x=120, y=5)


#Boton para iniciar
#le vamos a agregr un command para que cuando hagamos click se habiliten los botones
iniciar = Button(ventana,bg="#006",fg="white", text="Iniciar Juego",width=15,height=3,command = iniciarJ).place(x=130, y=350)
'''bloqueamos el tablero hasta que el participante de click en el boton iniciar,para eso creamos una funcion bloquear() que se va a llamar despues de q se haya creado toda la interfaz '''
bloquear()

ventana.mainloop()
#36:00
