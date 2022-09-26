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
            <title>Reporte de Resultados</title>
        </head>
        <body>
            <div class="p-3 mb-2 text-white" style="background-color:#9625b7">
                <h1><center>Reporte de Resultados</center></h1>
            </div>"""
def TablaOperaciones(Tokn):
    global cadena
    cadena += """<table class="table table-dark table-hover table-bordered">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Operación</th>
            <th scope="col">Números a operar</th>
            <th scope="col">Resultado</th>
        </tr>
    </thead>
    <tbody>"""
    contador = 1
    for tokn in Tokn:
        cadena += """
        <tr class="table-success">
            <th scope="row">""" + str(contador) + """</th>
            <th>""" + str(tokn.token) + """</th>
            <th>""" + str(tokn.ListaOperaciones) + """</th>
            <th>""" + str(tokn.ContadorTotales) + """</th>
        </tr>
        """
        contador +=1
    cadena += """</tbody>
    </table>"""

def CreacionDelArchivo():
    global cadena
    archivo=open("RESULTADOS_201902278.html","w", encoding="utf-8")
    archivo.write(cadena)
    archivo.close()
    os.startfile("RESULTADOS_201902278.html")

def GenerarArchivoDeOperaciones(Tokn):
    ComienzoReporte()
    TablaOperaciones(Tokn)
    CreacionDelArchivo()