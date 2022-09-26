class Token:
    def __init__(self, lexema,token,patron, linea, columna):
        self.lexema=lexema
        self.token=token
        self.patron=patron
        self.linea=linea
        self.columna=columna
    def ver(self):
        print("\n***********************************")
        print("Lexema: "+self.lexema)#Reporte de Tokens
        print("Token: "+self.token)
        print("Patron:" +self.patron)
        print("Linea: "+str(self.linea))
        print("Columna: "+str(self.columna))
        print("\n***********************************")


