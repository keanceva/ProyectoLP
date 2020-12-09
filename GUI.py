import tkinter as tk
from tkinter import scrolledtext as st
from lexicoLP import ImprimirAnalizar
from sintactico import prueba_sintactica
from sintactico import ImprimirSintactico

def text():
    datos = CajadeTexto.get("0.0", tk.END)
    return datos

def Analizar():
    dato= text()
    Analizador= ImprimirAnalizar(dato)
    print (Analizador)
    return Analizador

def Sintactico():
    dato= text()
    resultado= prueba_sintactica(dato)

    return resultado


def Ventana_2():
    ventana2 = tk.Tk()
    ventana2.geometry("700x500")
    Analizador = Analizar()
    etiqueta2 = tk.Label(ventana2, text = Analizador)
    etiqueta2.pack(side=tk.TOP)

def Ventana_3():
    ventana3 = tk.Tk()
    ventana3.geometry("700x500")
    resultado = Sintactico()
    if(len(resultado)==0):
        etiqueta3 = tk.Label(ventana3, text="No hay errores")
        etiqueta3.pack(side=tk.TOP)
    else:

        for i in resultado:
            linea="En la línea " + i
            etiqueta3 = tk.Label(ventana3, text =linea)
            etiqueta3.pack(side=tk.TOP)



ventana =tk.Tk()
ventana.geometry ("700x550")

logo= tk.PhotoImage(file='PHP-logo.svg')
logo= logo.subsample(5,5)
labelLogo= tk.Label(ventana,image=logo)
labelLogo.pack()

CajadeTexto = st.ScrolledText(ventana, width=50, height=20)

etiqueta = tk.Label(ventana, text = "Analizador Léxico" )
etiqueta.pack()

CajadeTexto.pack()

boton1 = tk.Button(text = "Analizar PHP", command= Ventana_2)
boton1.pack(padx=170,side=tk.LEFT)
boton2 = tk.Button(text = "Sintactico PHP", command= Ventana_3)
boton2.pack(side=tk.LEFT)
ventana.mainloop()
