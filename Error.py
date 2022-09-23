class Error:
    def __init__(self, lexema,tipo, columna,linea):
        self.lexema=lexema
        self.tipo=tipo
        self.columna=columna
        self.linea=linea
    def vererrores(self):
        print("\n***********************************")
        print("Descripción: "+self.lexema)
        print("Tipo: "+self.tipo)#Reporte de Tokens
        print("Columna: "+str(self.columna))
        print("Linea: "+str(self.linea))
        print("\n***********************************")