from pydoc import text
from re import A
from Token import *
from Error import *
from tkinter import messagebox
ListaAscii=["!","%","&","(",")","*","+","-",".",",",":",";","?","@","^","_","´","¨",'"',"'","~","{","}","Ç","ü","é","â","ä","à","å","ç","ê","ë","è","ï","î","Ä","Å","É","æ","Æ","ô","ö","ò","û","ù","ÿ","Ö","Ü","ø","£","Ø","×","ƒ","á","í","ó","ú","ñ","Ñ","ª","º","¿","®","¬","½","¼","¡","«","»","│","┤","Á","Â","À","©","╣","║","╗","╝","¢","¥","┐","└","┴","┬","├","─","┼","ã","Ã","╚","╔","╩","╦","╠","╬","ð","Ð","┌","+","-","*","²","³","¹","¾"]
ListaDeColores=["ROJO","VERDE","AZUL","MAGENTA","AMARILLO","CIAN","BLANCO","NEGRO","GRIS","ROSADO","NARANJA","ANARANJADO","ROSA","ROSADO","MORADO"]
ListaTabular=["\n"]
class Analizador:
    def __init__(self):
        self.ListaTokens=[]
        self.ListaErrores=[]
    def ascii(self,caracter):
        for i in range(32,256):
                if i!=60 and 61 and 62:
                    if chr(i)==caracter:
                        return True
    #Método para reconocer decimales
    def AutomataFinitoDecimal(self, caracter):
        EstadoAceptacion = [2]
        MiEstado = 0
        for abc in caracter:
            if MiEstado == 0:
                if abc.isdigit():
                    MiEstado = 1
                else:
                    MiEstado = -1
            elif MiEstado == 1:
                if abc.isdigit():
                    MiEstado = 1
                elif abc == ".":
                    MiEstado = 2
                else:
                    MiEstado =-1
            elif MiEstado == 2:
                if abc.isdigit():
                    MiEstado = 2
                else:
                    MiEstado = -1
            elif MiEstado ==-1:
                return False
        return MiEstado in EstadoAceptacion
    def AnalisisLexico(self, parametro):
        self.ListaTokens = []
        self.ListaErrores = []
        contador = 0
        linea = 1
        columna = 1
        lector = ""#buffer
        estado="A"#ESTADO INICIAL PARA PALABRAS RESERVADAS
        while contador<len(parametro):
            abc=parametro[contador]
            #INICIO ESTADO A-------TOKENS
            if estado == "A":
                if (abc == "<"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"menor","<",linea,columna))
                    lector=""
                    estado="A"
                elif (abc==">"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"mayor",">",linea,columna))
                    lector=""
                    estado="A"
                elif (abc=="="):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"igual","=",linea,columna))
                    lector=""
                    estado="A"
                elif (abc=="/"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"diagonal","/",linea,columna))
                    lector=""
                    estado="A"
                elif (abc == "["):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"corcheteabre","[",linea,columna))
                    lector=""
                    estado="A"
                elif (abc == "]"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"corchetecierra","]",linea,columna))
                    lector=""
                    estado="A"
                elif (abc.isalpha()) and (not abc.isdigit()):#ISALPHA ENCUENTRA PALABRA Y ALMACENA
                    lector=abc
                    columna+=1
                    estado="B"
                elif (abc.isdigit()):#ISDIGIT ENCUENTRA DIGITOS Y ALMACENA
                    lector=abc
                    columna+=1
                    estado="C"
                elif abc == '"':#SE TOMA EL COMENTARIO COMO UNA CADENA
                    lector=abc
                    columna+=1
                    estado="D"
                elif abc == '\n':
                    columna = 1
                    linea +=1
                elif abc == ' ':#" "
                    columna+=1
                elif abc == '\t' or abc=="\r":
                    columna+=1
                else:
                    self.ListaErrores.append(Error(lector,"Error",linea,columna))
                    lector=""
                    columna+=1
            #INICIO ESTADO B
            elif estado == "B" :#PUEDEN VENIR LETRAS Y NUMEROS
                if (abc.isalpha()) or (abc in ListaAscii) and (not abc.isdigit()):
                    lector+=abc
                    columna+=1
                    estado="B"
                else:
                    if (lector in ListaDeColores):
                        self.ListaTokens.append(Token(lector,"RColores","colores",linea,columna))
                    elif (lector == "Tipo"):
                        self.ListaTokens.append(Token(lector,"RTipo","Tipo",linea,columna))
                    elif (lector == "Operacion"):
                        self.ListaTokens.append(Token(lector,"ROperacion","Operacion",linea,columna))
                    elif (lector == "SUMA"):
                        self.ListaTokens.append(Token(lector,"RSUMA","Suma",linea,columna))
                    elif (lector == "RESTA"):
                        self.ListaTokens.append(Token(lector,"RRESTA","Resta",linea,columna))
                    elif (lector == "MULTIPLICACION"):
                        self.ListaTokens.append(Token(lector,"RMULTIPLICACION","Multiplicacion",linea,columna))
                    elif (lector == "DIVISION"):
                        self.ListaTokens.append(Token(lector,"RDIVISION","Division",linea,columna))
                    elif (lector == "POTENCIA"):
                        self.ListaTokens.append(Token(lector,"RPOTENCIA","Potencia",linea,columna))
                    elif (lector == "RAIZ"):
                        self.ListaTokens.append(Token(lector,"RRAIZ","Raiz",linea,columna))
                    elif (lector == "INVERSO"):
                        self.ListaTokens.append(Token(lector,"RINVERSO","Inverso",linea,columna))
                    elif (lector == "SENO"):
                        self.ListaTokens.append(Token(lector,"RSENO","Seno",linea,columna))  
                    elif (lector == "COSENO"):
                        self.ListaTokens.append(Token(lector,"RCOSENO","Coseno",linea,columna))   
                    elif (lector == "TANGENTE"):
                        self.ListaTokens.append(Token(lector,"RTANGENTE","Tangente",linea,columna))
                    elif (lector == "MOD"):
                        self.ListaTokens.append(Token(lector,"RMOD","Mod",linea,columna))     
                    elif (lector == "Numero"):
                        self.ListaTokens.append(Token(lector,"RNumero","Numero",linea,columna))
                    elif (lector == "Texto"):
                        self.ListaTokens.append(Token(lector,"RTexto","Texto",linea,columna))
                    elif (lector == "Funcion "):
                        self.ListaTokens.append(Token(lector,"RFuncion ","Funcion",linea,columna))
                    elif (lector == "ESCRIBIR"):
                        self.ListaTokens.append(Token(lector,"RESCRIBIR ","Escribir",linea,columna))
                    elif (lector == "Titulo"):
                        self.ListaTokens.append(Token(lector,"RTitulo","Titulo",linea,columna))
                    elif (lector == "Operaciones"):
                        self.ListaTokens.append(Token(lector,"ROperaciones","Operaciones",linea,columna))
                    elif (lector == "Descripcion"):
                        self.ListaTokens.append(Token(lector,"RDescripcion","Descripcion",linea,columna))
                    elif (lector == "TEXTO"):
                        self.ListaTokens.append(Token(lector,"RTEXTO","Texto",linea,columna))
                    elif (lector == "Contenido"):
                        self.ListaTokens.append(Token(lector,"RContenido","Contenido",linea,columna)) 
                    elif (lector == "TIPO"):
                        self.ListaTokens.append(Token(lector,"RTIPO","Tipo",linea,columna))  
                    elif (lector == "Estilo"):
                        self.ListaTokens.append(Token(lector,"REstilo","Estilo",linea,columna)) 
                    elif (lector == "Titulo Color"):
                        self.ListaTokens.append(Token(lector,"RTituloColor","TituloColor",linea,columna)) 
                    elif (lector == "Tamanio"):
                        self.ListaTokens.append(Token(lector,"RTamanio","Tamanio",linea,columna))
                    elif (lector == "Descripcion Color"):
                        self.ListaTokens.append(Token(lector,"RDescripcionColor","DescripcionColor",linea,columna))
                    elif (lector == "Contenido Color"):
                        self.ListaTokens.append(Token(lector,"RContenidoColor","ContenidoColor",linea,columna))
                    lector=""
                    estado="A"
                    contador-=1
            elif estado == "C":#numeros
                if abc.isdigit():
                    lector+=abc
                    columna+=1
                    estado="C"
                elif abc == ".":
                    lector+=abc
                    columna+=1
                    estado="C"
                else:
                    if self.AutomataFinitoDecimal(abc):
                        self.ListaTokens.append(Token(lector,"Double","\d\d*\.\d\d*",linea,columna))
                    else:
                        self.ListaTokens.append(Token(lector,"Entero","\d\d*",linea,columna))
                    lector = ""
                    contador -= 1
                    estado = "A"
                    #EN UN NUEVO ESTADO TOMAR TOKENS CON [] Y TEXTO CON []
            elif estado == "D" :
                if abc == '"':
                    lector+=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"Comentario","texto",linea,columna))
                    lector=""
                    estado = "A"
                elif abc == '\n':
                    columna = 1
                    linea +=1
                else:
                    lector+=abc
                    columna+=1
                    estado="D"
            contador+=1
    def impresion(self):
        print("TOKENS: ")
        for Tokkens in self.ListaTokens:
            Tokkens.ver()
        print("")
        print("ERRORES: ")
        for Errrores in self.ListaErrores:
            Errrores.vererrores()
        print("Cantidad de Tokens en el Texto: "+str(len(self.ListaTokens)))
        print("Cantidad de Errores en el Texto: "+str(len(self.ListaErrores)))
