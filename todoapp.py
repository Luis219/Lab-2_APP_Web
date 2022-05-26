#se importa escape de markupsafe

import re
import json
import os
from asyncio import mixins
from markupsafe import escape

#Se importa la librería Flask
from flask import Flask, abort, redirect, render_template, request, flash, url_for

#variable de instancia app
app=Flask(__name__, template_folder='templates')

app.secret_key='12345'


#Ruta raíz- página inicio
@app.route('/')

#función que retorna la página principal
def inicio():
    return render_template('inicio.html')


tareas=[]
correos=[]
prioridades=[]

#Ruta hacia la función enviar

@app.route('/enviar',methods=['POST'])

#función que permite enviar los datos ingresados hacia la tabla
def enviar(): 
    tarea= request.form.get('tarea')
    correo= request.form.get('correo')
    prioridad= request.form.get('prioridad')
  

    #validar que se ingresen datos
    if len(tarea)>0 and len(correo)>0:
       
       #se ingresen los datos a las listas
        tareas.append(tarea)
        correos.append(correo)
        prioridades.append(prioridad)
    else:
        flash('Error al ingresar los datos')
        return render_template('inicio.html')
 
    return render_template('inicio.html', tareas=tareas, correos=correos, prioridades= prioridades)

#Ruta hacia función borrar
@app.route('/borrar',methods=['POST'])

#función que permite borrar las tareas de toda la tabla
def borrar():
    
    tareas.clear()
    correos.clear()
    prioridades.clear()

    return render_template('inicio.html',tareas=tareas, correos=correos, prioridades= prioridades)

@app.route('/guardar',methods=['POST'])

#función que permite borrar las tareas de toda la tabla
def guardar():

    tarea= request.form.get('tarea')
    correo= request.form.get('correo')
    prioridad= request.form.get('prioridad')

    tareas.append(tarea)
    correos.append(correo)
    prioridades.append(prioridad)

   
  
    path, _=os.path.split(os.path.abspath(__file__))
    
    data={}
    data['tareas']=[]
    data['correos']=[]
    data['prioridad']=[]    
    
    data["tareas"].append(tareas)
    data["correos"].append(correos)
    data["prioridad"].append(prioridades)

   
    with open(path+f'/datos.json','w') as file:
        json.dump(data, file, indent=4)

    return render_template('guardar.html')


@app.route('/ver_datos',methods=['POST'])

#función que permite borrar las tareas de toda la tabla
def ver_datos():
    
    path, _=os.path.split(os.path.abspath(__file__))
    
   
    with open(path+'/datos.json') as file:
       data= json.load(file)
    
    flash(data)

    return render_template('guardar.html')



#función principal
if __name__=='__main__':
    app.run(debug=True)
    


