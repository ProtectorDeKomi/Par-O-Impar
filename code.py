import tkinter as tk
from tkinter import *

def main(self):
    global text,output
    """
    Main function
    Esta Funcion Crea Una Instancia De Tkinter y Carga Los Elementos Correspodientes 
    ======== La Funcion Recibe El Parametro Self Y Este Es Una Llamada A La Clase TK de La Libreria Tkinter =====
    """
    self.config(width=300, height=130)
    self.title("Par O Impar By Astartes")
    self.resizable(False,False)
    Label(self,text="Introduce Tu Numero").place(x=0, y=5)
    output = Label(self)
    output.config(text="")
    output.place(x=5,y=50)
    text = Text(self,width=15,height=1)
    text.place(x=5,y=30)
    button = Button(self, text="Cerrar",command=self.destroy)
    button.place(x=255,y=100)
    button = Button(self,command=brain)
    button.config(text="Comprobar")
    button.place(x=5,y=100)
    self.mainloop()
def brain():
    """
    Esta Funcion Calcula Un Numero Entero y Determina Si Es Un Numero Par O Impar Y Muestra El Resultado
    """
    var = text.get(1.0, "end-1c")
    if int(var) % 2 == 0:
        return output.config(text=f"\n{var} Es Un Numero Par",foreground="Green")
    else:
        return output.config(text=f"\n{var} Es Un Numero Impar",foreground="Red")

if __name__ == "__main__":
    main(tk.Tk())