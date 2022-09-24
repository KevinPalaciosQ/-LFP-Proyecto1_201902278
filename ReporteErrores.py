import os
cadena = ""

def ComienzoReporte():
    global cadena
    cadena += """<!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <link rel="shortcut icon" href="Icono.ico">
            <title>Reporte de Errores</title>
        </head>
        <body>
            <div class="p-3 mb-2 text-white" style="background-color:#c51212">
                <h1><center>Reporte de Errores</center></h1>
            </div>"""

def TablaErrores(Fallo):
    global cadena
    cadena += """<table class="table table-dark table-hover table-bordered">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Tipo de Error</th>
            <th scope="col">Caracter(es)</th>
            <th scope="col">Linea</th>
            <th scope="col">Columna</th>
        </tr>
    </thead>
    <tbody>"""
    conteo = 1
    for fallo in Fallo:
        cadena += """
        <tr class="table-danger">
            <th scope="row">""" + str(conteo) + """</th>
            <th>""" + str(fallo.tipo) + " Lexico" + """</th>
            <th>""" + str(fallo.lexema) + """</th>
            <th>""" + str(fallo.linea) + """</th>
            <th>""" + str(fallo.columna) + """</th>
        </tr>
        """
        conteo +=1
    cadena += """</tbody>
    </table>"""

def CreacionDelArchivo():
    global cadena
    archivo=open('Errores_201902278.html','w', encoding='utf-8')
    archivo.write(cadena)
    archivo.close()
    os.startfile("Errores_201902278.html")

def GenerarArchivoDeErrores(Fallo):
    ComienzoReporte()
    TablaErrores(Fallo)
    CreacionDelArchivo()