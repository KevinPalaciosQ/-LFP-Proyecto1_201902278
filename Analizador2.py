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

    #Método para reconocer decimales
    def AutomataFinitoDecimal(self, caracter):
        Estado_aceptacion = [2]
        MiEstado = 0
        for abc in caracter:
            if MiEstado ==0:
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
        return MiEstado in Estado_aceptacion

    def AnalisisLexico(self, dato):
        self.ListaTokens = []
        self.ListaErrores = []
        contador = 0
        linea = 1
        columna = 1
        lector = ""#buffer
        estado="S0"#ESTADO INICIAL PARA PALABRAS RESERVADAS
        while contador<len(dato):
            abc=dato[contador]
            #INICIO ESTADO S0-------TOKENS
            if estado == "S0":
                if (abc == "<"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"menor","<",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc==">"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"mayor",">",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc=="="):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"igual","=",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc=="/"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"diagonal","/",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc == "["):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"corcheteabre","[",linea,columna))
                    lector=""
                    estado="S0"
                elif (abc == "]"):
                    lector=abc
                    columna+=1
                    self.ListaTokens.append(Token(lector,"corchetecierra","]",linea,columna))
                    lector=""
                    estado="S0"
                
                elif (abc.isalpha()) and (not abc.isdigit()):#ISALPHA ENCUENTRA PALABRA Y ALMACENA
                    lector=abc
                    columna+=1
                    estado="S1"
                elif (abc.isdigit()):#ISDIGIT ENCUENTRA DIGITOS Y ALMACENA
                    lector=abc
                    columna+=1
                    estado="S2"
            
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
            #INICIO ESTADO S1
            elif estado == "S1" :#PUEDEN VENIR LETRAS Y NUMEROS
                if (abc.isalpha()) or (abc in ListaAscii) and (not abc.isdigit()):
                    lector+=abc
                    columna+=1
                    estado="S1"
                else:
                    if (lector in ListaDeColores):
                        self.ListaTokens.append(Token(lector,"RColores","colores",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Tipo"):
                        self.ListaTokens.append(Token(lector,"RTipo","Tipo",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Operacion"):
                        self.ListaTokens.append(Token(lector,"ROperacion","Operacion",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "SUMA"):
                        self.ListaTokens.append(Token(lector,"RSUMA","Suma",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "RESTA"):
                        self.ListaTokens.append(Token(lector,"RRESTA","Resta",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "MULTIPLICACION"):
                        self.ListaTokens.append(Token(lector,"RMULTIPLICACION","Multiplicacion",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "DIVISION"):
                        self.ListaTokens.append(Token(lector,"RDIVISION","Division",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "POTENCIA"):
                        self.ListaTokens.append(Token(lector,"RPOTENCIA","Potencia",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "RAIZ"):
                        self.ListaTokens.append(Token(lector,"RRAIZ","Raiz",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "INVERSO"):
                        self.ListaTokens.append(Token(lector,"RINVERSO","Inverso",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "SENO"):
                        self.ListaTokens.append(Token(lector,"RSENO","Seno",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1  
                    elif (lector == "COSENO"):
                        self.ListaTokens.append(Token(lector,"RCOSENO","Coseno",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1   
                    elif (lector == "TANGENTE"):
                        self.ListaTokens.append(Token(lector,"RTANGENTE","Tangente",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "MOD"):
                        self.ListaTokens.append(Token(lector,"RMOD","Mod",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1     
                    elif (lector == "Numero"):
                        self.ListaTokens.append(Token(lector,"RNumero","Numero",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Texto"):
                        self.ListaTokens.append(Token(lector,"RTexto","Texto",linea,columna))
                        lector=""
                        if self.ListaTokens[len(self.ListaTokens) - 2].token == "menor" and abc == ">":
                            self.ListaTokens.append(Token(abc,"mayor",">",linea,columna))
                            contador += 1
                            estado = "S3" 
                        else:
                            lector=""
                            estado="S0"
                            contador-=1
                        
                    elif (lector == "Funcion"):
                        self.ListaTokens.append(Token(lector,"RFuncion ","Funcion",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "ESCRIBIR"):
                        self.ListaTokens.append(Token(lector,"RESCRIBIR ","Escribir",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    elif (lector == "Titulo"):
                        self.ListaTokens.append(Token(lector,"RTitulo","Titulo",linea,columna))
                        lector=""
                        if self.ListaTokens[len(self.ListaTokens) - 2].token == "menor" and abc == ">":
                            self.ListaTokens.append(Token(abc,"mayor",">",linea,columna))
                            contador += 1
                            estado = "S3" 
                        else:
                            lector=""
                            estado="S0"
                            contador-=1
                    elif (lector == "Operaciones"):
                        self.ListaTokens.append(Token(lector,"ROperaciones","Operaciones",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1

                    elif (lector == "Descripcion"):
                        self.ListaTokens.append(Token(lector,"RDescripcion","Descripcion",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1

                    elif (lector == "TEXTO"):
                        self.ListaTokens.append(Token(lector,"RTEXTO","Texto",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1

                    elif (lector == "TIPO"):
                        self.ListaTokens.append(Token(lector,"RTIPO","Tipo",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1  

                    elif (lector == "Estilo"):
                        self.ListaTokens.append(Token(lector,"REstilo","Estilo",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1 

                    elif (lector == "Color"):
                        self.ListaTokens.append(Token(lector,"RColor","Color",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1

                    elif (lector == "Tamanio"):
                        self.ListaTokens.append(Token(lector,"RTamanio","Tamanio",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1

                    elif (lector == "Descripcion"):
                        self.ListaTokens.append(Token(lector,"RDescripcion","Descripcion",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1

                    elif (lector == "Contenido"):
                        self.ListaTokens.append(Token(lector,"RContenido","Contenido",linea,columna))
                        lector=""
                        estado="S0"
                        contador-=1
                    else:
                        self.ListaErrores.append(Error(lector,"Error",linea,columna))
                        lector=""
                        columna+=1
            #INICIO ESTADO S2     
            elif estado == "S2":#Numeros
                if abc.isdigit():
                    lector+=abc
                    columna+=1
                    estado="S2"
                elif abc == ".":
                    lector+=abc
                    columna+=1
                    estado="S2"
                else:
                    if self.AutomataFinitoDecimal(abc):
                        self.ListaTokens.append(Token(lector,"Double","\d\d*\.\d\d*",linea,columna))
                    else:
                        self.ListaTokens.append(Token(lector,"Entero","\d\d*",linea,columna))
                    lector = ""
                    contador -= 1
                    estado = "S0"
            #INICIO ESTADO S3
            elif estado == "S3":#Textos entre abrebiaturas
                if abc != "<":
                    lector += abc
                    columna += 1
                    estado = "S3"

                elif abc == "\n":
                    lector += abc
                    linea += 1
                    columna = 1
                    estado = "S3"

                else:
                    self.ListaTokens.append(Token(lector, "cadena", ".[^<]", linea, columna))
                    lector = ""
                    estado = "S0"
                    contador -= 1

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