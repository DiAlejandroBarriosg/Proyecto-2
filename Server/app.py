from logging import debug
from flask import Flask, json, request, jsonify
from flask_cors import CORS
from CRUD_Usuarios import CRUD_Usuario
from datetime import datetime

# Inicializar flask
crud_usuarios = CRUD_Usuario()
app = Flask(__name__)
CORS(app)

# Métodos de peticiones

# GET -> recuperar informacion
# POST -> enviar informacion
# DELETE -> eliminar informacion
# PUT -> insertar informacion

# Códigos de HTTP

# 200 -> ok
# 201 -> objeto creado
# 400 -> peticion incorrecta
# 404 -> no se encontro

# Insertar nuevo usuario
@app.route('/usuario', methods=["PUT"])
def insertarUsuario():

    # Parametros que nos envia el frontend
    correo = request.json["correo"]
    pwd = request.json["pwd"]
    nombre = request.json["nombre"]
    edad = request.json["edad"]

    resultado = crud_usuarios.createUsuario(correo, pwd, nombre, edad)
    return jsonify({"data": resultado, "mensaje": "OK"}), 200

# Login
@app.route('/login', methods=["POST"])
def login():

    # Parametros que nos envia el frontend
    correo = request.json["correo"]
    pwd = request.json["pwd"]

    resultado = crud_usuarios.login(correo, pwd)

    if resultado:
        return jsonify({"data": resultado, "mensaje": "OK"}), 200
    else:
        return jsonify({"mensaje": "Credenciales incorrectas"}), 404

# Carga masiva
@app.route('/usuarios/carga-masiva', methods=["POST"])
def cargaMasiva():

    # Parametros que nos envia el frontend
    print(request)
    usuarios = request.json["usuarios"]
    print(request.json['usuarios'])
    resultado = crud_usuarios.cargaMasiva(usuarios)
    print(resultado)
    if resultado == "OK":
        return jsonify({"data": crud_usuarios.readUsuarios(), "mensaje": "OK"}), 200
    else:
        return jsonify({"mensaje": "Hubo un error en la carga masiva"}), 400

# Recuperar usuarios
@app.route('/usuarios', methods=["GET"])
def recuperarUsaurios():
    arreglo = crud_usuarios.readUsuarios()
    return jsonify({"data": arreglo, "mensaje": "OK"}), 200

# Reporte edades
@app.route('/usuarios/reporte', methods=["GET"])
def reporteEdades():
    res = crud_usuarios.reporteEdades()
    return jsonify({"data": res, "mensaje": "OK"}), 200



if __name__ == '__main__':
    app.run(debug=True, port=4001)
