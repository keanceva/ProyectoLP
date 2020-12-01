import tkinter
from tkinter import scrolledtext as st



ventana =tkinter.Tk()
ventana.geometry ("500x400")
scrolledtext1 = st.ScrolledText(ventana, width=50, height=10)
etiqueta = tkinter.Label(ventana, text = "Analizador Léxico")
etiqueta.pack()

cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()

boton1 = tkinter.Button(ventana, text = "Analizar")
boton1.pack()





ventana.mainloop()
