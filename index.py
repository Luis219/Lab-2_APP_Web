#se importa escape de markupsafe

from asyncio import mixins
from markupsafe import escape

#Se importa la librería Flask
from flask import Flask, abort, render_template

#variable de instancia app
app=Flask(__name__, template_folder='templates')

#Ruta raíz
@app.route('/')

#Ruta página de inicio html
@app.route('/inicio')

#función que retorna la página
def inicio():
    return render_template('inicio.html')



#función principal
if __name__=='__main__':
    app.run(debug=True)
    


