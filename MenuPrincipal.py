import tkinter
from tkinter import *
from tkinter import font 
from tkinter import ttk 
import tkinter as ttk
from tkinter import filedialog
from tkinter import messagebox 
import webbrowser as wb
from Token import Token
from Error import Error
from ReporteErrores import *
from ReporteTokens import *
ventanaprincipal = None
global textbox
global RutaArchivo
material = ""
hola = ""
from Analizador2 import *
def ObtenerRuta():
    global textbox
    global RutaArchivo
    global material
    try:
        RutaArchivo = filedialog.askopenfilename(title="Cargar Archivo", filetypes = (("Text files", "*.lfp*"), ("all files", "*.*")))
        ruta2 = open(RutaArchivo,"r",encoding="utf-8")
        material = ruta2.read()
        print(material)
        textbox.insert(END, str(material))
        messagebox.showinfo("Succes","Se Cargó el Archivo")
    except:
        messagebox.showwarning("Advertencia","No se pudo Cargar el Archivo")
def Guardar():
    global RutaArchivo
    global textbox
    try:
        ruta = open(RutaArchivo,"w",encoding="utf8")
        ruta.write(textbox.get(1.0,END))
        ruta.close()
        messagebox.showinfo("Succes","Se Guardo el Archivo")
    except:
        messagebox.showwarning("Advertencia","No se pudo guardar el Archivo")
def GuardarComo():
    global textbox
    try:
        ruta = filedialog.asksaveasfile(title="Guardar Archivo", filetypes = (("Text files", "*.lfp*"), ("all files", "*.*")))
        if ruta:
            MiTexto = textbox.get(1.0,END)
            ruta.write(MiTexto)
            ruta.close()
            messagebox.showinfo("Succes","Se Guardo el Archivo")
    except:
            messagebox.showwarning("Advertencia","No se pudo guardar el Archivo")
def Analizadorr():
    global material
    global hola
    hola=Analizador()
    hola.AnalisisLexico(material)
    hola.impresion()
def Errores():
    global hola
    global material
    hola=Analizador()
    hola.AnalisisLexico(material)
    GenerarArchivoDeErrores(hola.ListaErrores)
def Tokens():
    global hola
    global material
    hola=Analizador()
    hola.AnalisisLexico(material)
    GenerarArchivoDeTokens(hola.ListaTokens)
def Abrir():
    ObtenerRuta()
def Salir():
    global VentanaAyuda
    VentanaAyuda.destroy()
    VentanaPrincipal()
def ManualTecnico():
    wb.open_new(r"C:\Users\kevin\OneDrive\Documentos\-LFP-Proyecto1_201902278\Manualtecnico.pdf")
def ManualDeUsuario():
    wb.open_new(r"C:\Users\kevin\OneDrive\Documentos\-LFP-Proyecto1_201902278\ManualUsuario.pdf")
def VentanaDeAyuda():
    ventanaprincipal.destroy()
    global VentanaAyuda
    VentanaAyuda = tkinter.Tk()
    VentanaAyuda.title("Temas de Ayuda")
    VentanaAyuda.geometry("1000x400")
    VentanaAyuda.config(bg="light cyan")
    VentanaAyuda.resizable(0,0)
    #ETIQUETAS
    lbldatoscurso = Label(VentanaAyuda,text="Nombre del Curso: Lab Lenguajes Formales y de Programación          Sección B+",font="Cambria 22", fg="SteelBlue4", bg="light cyan")
    lbldatoscurso.place(x=10,y=10)
    lbldatosestudiante = Label(VentanaAyuda,text="Nombre del Estudiante: Kevin Estuardo Palacios Quiñonez",font="Cambria 22", fg="SteelBlue4", bg="light cyan")
    lbldatosestudiante.place(x=10,y=60)
    lblcarne = Label(VentanaAyuda,text="Carné del Estudiante: 201902278",font="Cambria 22", fg="SteelBlue4", bg="light cyan")
    lblcarne.place(x=10,y=110)
    
    #BOTONES AYUDA
    botonregresar= Button(VentanaAyuda,text="Regresar",fon="arial 20", fg="gray24", bg="powder blue", relief="groove", bd=9, width=14,command=Salir)
    botonregresar.place(x=650,y=300)
    VentanaAyuda.mainloop()
def VentanaPrincipal():
    global ventanaprincipal
    global textbox
    ventanaprincipal = tkinter.Tk()
    ventanaprincipal.title("")
    ventanaprincipal.geometry("1000x700")
    ventanaprincipal.config(bg="light cyan")
    ventanaprincipal.resizable(0,0)
    #MENU
    menubar = Menu(ventanaprincipal)
    ventanaprincipal.config(menu=menubar)
    #CREACION DEL MENU 
    file_menu = Menu(menubar,tearoff=False)
    help_menu = Menu(menubar, tearoff=0)
    #ITEMS DEL MENU
    file_menu.add_command(label="Abrir", command=Abrir)
    file_menu.add_command(label="Guardar", command=Guardar)
    file_menu.add_command(label="Guardar Como", command=GuardarComo)
    file_menu.add_command(label="Analizar", command=Analizadorr)
    file_menu.add_command(label="Reporte de Errores",command=Errores)
    file_menu.add_command(label="Reporte de Tokens",command=Tokens)
    file_menu.add_command(label="Salir",command=ventanaprincipal.destroy)
    #ITEMS DEL MENU AYUDA
    help_menu.add_command(label="Manual de Usuario", command=ManualDeUsuario)
    help_menu.add_command(label="Manual Técnico", command=ManualTecnico)
    help_menu.add_command(label="Temas de Ayuda",command=VentanaDeAyuda)
    #AÑADIR MENU A LA BARRA
    menubar.add_cascade(label="Menú",menu=file_menu)
    menubar.add_cascade(label="?",menu=help_menu)
    #ETIQUETAS
    lblentrada = Label(ventanaprincipal,text="Entrada:",font="Cambria 22", fg="SteelBlue4", bg="light cyan")
    lblentrada.place(x=100,y=-5)
    lblsalida = Label(ventanaprincipal,text="Salida:",font="Cambria 22", fg="SteelBlue4", bg="light cyan")
    lblsalida.place(x=550,y=-5)
    #TEXTBOX
    textbox = Text(ventanaprincipal, width=50, height=40,bg="floral white")
    textbox.place(x=100,y=30)
    textboxsalida = Text(ventanaprincipal, width=50, height=40,bg="light steel blue")
    textboxsalida.place(x=550,y=30)
    ventanaprincipal.mainloop()
VentanaPrincipal()