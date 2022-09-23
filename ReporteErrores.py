import os
texto = ""

def ComienzoReporte():
    global texto
    texto += """<!doctype html>
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

def TablaErrores(Error):
    global texto
    texto += """<table class="table table-dark table-hover table-bordered">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Lexema</th>
            <th scope="col">Tipo</th>
            <th scope="col">Columna</th>
            <th scope="col">Fila</th>
        </tr>
    </thead>
    <tbody>"""
    contador = 1
    for error in Error:
        texto += """
        <tr class="table-danger">
            <th scope="row">""" + str(contador) + """</th>
            <th>""" + str(error.lexema) + """</th>
            <th>""" + str(error.tipo) + """</th>
            <th>""" + str(error.columna) + """</th>
            <th>""" + str(error.fila) + """</th>
        </tr>
        """
        contador +=1
    texto += """</tbody>
    </table>"""

def CreacionDelArchivo():
    global texto
    archivo=open('Errores_201902278.html','w', encoding='utf-8')
    archivo.write(texto)
    archivo.close()
    os.startfile("Errores_201902278.html")

def GenerarArchivoDeErrores(Error):
    ComienzoReporte()
    TablaErrores(Error)
    CreacionDelArchivo()