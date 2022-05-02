from flask import Flask, request, render_template, url_for, redirect, jsonify, session
from werkzeug.exceptions import abort

app = Flask(__name__)

app.secret_key = 'mi llave secreta'  # llave para usar las sesiones


@app.route('/')
def inicio():
    if 'username' in session:
        # session["Username"]  almacena el nombre del usuario
        return f'''El usuario ha hecho login {session["username"]}'''
    # app.logger.info(f'Entramos al path/{request.path}')
    return '''<title>Index</title> hola mundo ji '''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # OMITIMOS VALIDACION DE USER AND PASSW
        usuario = request.form['username']  # ese username es que sale en el atributo name de la etiqueta input
        # agregar el usuario a la sesion
        session['username'] = usuario
        # session['username'] = request.form['username']

        return redirect(url_for('inicio'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/saludar/<nombre>')
# Crea un path para la app si pongo /saludar en el navegador me sale la nueva pagina

def saludar(nombre):
    return f'<title>Saludo</title>Saludos {nombre.upper()}'


# 127.0.0.1:5000/(Nombre)
# y saluda al nombre que yo introduzca

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return render_template('edad.html', edad=45)


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)


@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Travis '))


@app.route('/salir')
def salir():
    return abort(404)


@app.route('/api//mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre}
    return jsonify(valores)


@app.errorhandler(404)
def pagnotfound(error):
    return render_template('err404.html', error=error), 404


if __name__ == '__main__':
    app.run()
