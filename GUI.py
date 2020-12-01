import tkinter as tk
from tkinter import scrolledtext as st
from lexicoLP import ImprimirAnalizar

def text():
    datos = CajadeTexto.get("0.0", tk.END)
    return datos

def Analizar():
    dato= text()
    Analizador= ImprimirAnalizar(dato)
    print (Analizador)
    return Analizador



def Ventana_2():
    ventana2 = tk.Tk()
    ventana2.geometry("700x500")
    Analizador = Analizar()
    etiqueta2 = tk.Label(ventana2, text = Analizador)
    etiqueta2.pack(side=tk.TOP)



ventana =tk.Tk()
ventana.geometry ("500x400")

CajadeTexto = st.ScrolledText(ventana, width=50, height=20)

etiqueta = tk.Label(ventana, text = "Analizador Léxico" )
etiqueta.pack()


CajadeTexto.pack()

boton1 = tk.Button(text = "Analizar PHP", command= Ventana_2)
boton1.pack()
ventana.mainloop()
