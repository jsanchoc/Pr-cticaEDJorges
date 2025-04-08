# IMPORTACION DE LIBRERIAS
from flask import Flask, request, jsonify
from flask_cors import CORS
from JGVutils import SQLiteConnection

# CONFIGURACION DEL PROYECTO
application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

# PAGINAS PARA QUE ME APAREZCA UNA PAG INICIO
@application.route("/", methods=("GET","POST"))
def inicio():
    with open("HTML/index.html", encoding = "utf-8") as f:
        return f.read()

@application.route("/peliculas", methods=("GET"))
def conexion():
    conexion = SQLiteConnection("Database1.db")
    peliculas = conexion.execute_query("SELECT * FROM peliculas")
    return peliculas

@application.route("/agregar",methods =("POST"))
def agregar_pelicula():
    # RECOGEMOS LOS DATOS DEL FORMULARIO ENVIADO
    codigo = request.form.get("codigo")
    genero = request.form.get("genero")
    edad = request.form.get("edad")
    director = request.form.get("director")
    titulo = request.form.get("titulo")

    # INSERTAMOS LA BASE DE DATOS
    conexion = SQLiteConnection("Database1.db")
    conexion.execute_query(
        f"INSERT INTO peliculas(codigo,genero,edad,director,titulo)"
        (codigo,genero,edad,director,titulo)
    )

    return "Película agregada correctamente."

if __name__ == "__main__"
    application.run(debug=True)
