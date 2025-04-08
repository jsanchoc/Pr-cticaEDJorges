# IMPORTACION DE LIBRERIAS
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection

# CONFIGURACION DEL PROYECTO
application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

# PAGINAS PARA QUE ME APAREZCA UNA PAG INICIO
@application.route("/", methods=["GET","POST"])
def inicio():
    # Lectura del archivo html
    with open("HTML/index.html", encoding = "utf-8") as f:
        return f.read()

# RUTA PARA AGREGAR LA PELICULA
@application.route("/agregar",methods =["POST"])
def agregar_pelicula():
    # RECOGEMOS LOS DATOS DEL FORMULARIO ENVIADO
    codigo = request.form.get("codigo")
    genero = request.form.get("genero")
    edad = request.form.get("edad")
    director = request.form.get("director")
    titulo = request.form.get("titulo")

    if not(codigo AND genero AND edad AND director AND titulo):
        return "Error: Todos los campos son requeridos"

    # INSERTAMOS LA BASE DE DATOS
    conexion = SQLiteConnection("Database1.db")
    conexion.execute_query(
        f"INSERT INTO peliculas(codigo,genero,edad,director,titulo) VALUES(?,?,?,?,?)",

        ## CADA ? hace referencia a cada uno de los parametros dentro de peliculas
        (codigo,genero,edad,director,titulo)
    )

    return "Película agregada correctamente."

if __name__ == "__main__":
    application.run(debug=True)
