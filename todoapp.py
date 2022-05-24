#se importa escape de markupsafe
import re
from asyncio import mixins
from markupsafe import escape

#Se importa la librería Flask
from flask import Flask, abort, render_template, request

#variable de instancia app
app=Flask(__name__, template_folder='templates')

#Ruta raíz- página inicio
@app.route('/')

#función que retorna la página
def inicio():
    return render_template('inicio.html')

#Ruta raíz- página enviar con metodo get
@app.route('/enviar',methods=['POST'])

#función que retorna la página enviar
def enviar():

    tarea= request.form.get('tarea')
    correo= request.form.get('correo')
    prioridad= request.form.get('prioridad')
    tareas=[]
    tareas.append(tarea)
 
    correos=[]
    correos.append(correo)
    
    prioridades=[]
    prioridades.append(prioridad)
   



    def validar_correo(correo):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(expresion_regular, correo) is not None
    return render_template('inicio.html', tareas, correos, prioridades)

#Ruta raíz- página borrar
@app.route('/borrar')

#función que retorna la página borrar
def borrar():

    return render_template('borrar.html')


#función principal
if __name__=='__main__':
    app.run(debug=True)
    


