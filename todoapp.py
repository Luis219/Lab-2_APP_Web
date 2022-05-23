#se importa escape de markupsafe

from asyncio import mixins
from markupsafe import escape

#Se importa la librería Flask
from flask import Flask, abort, render_template

#variable de instancia app
app=Flask(__name__, template_folder='templates')

#Ruta raíz- página inicio
@app.route('/')

#función que retorna la página
def inicio():
    return render_template('inicio.html')

#Ruta raíz- página enviar
@app.route('/enviar')

#función que retorna la página enviar
def enviar():
    return render_template('enviar.html')

#Ruta raíz- página borrar
@app.route('/borrar')

#función que retorna la página borrar
def borrar():
    return render_template('borrar.html')


#función principal
if __name__=='__main__':
    app.run(debug=True)
    


