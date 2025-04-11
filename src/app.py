# IMPORTACIÓN DE LIBRERÍAS
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection


# CONFIGURACIÓN DEL PROYECTO
application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

# PÁGINAS PARA QUE ME APAREZCA UNA PAG INICIO
@application.route("/", methods=["GET"])
def inicio():
    # Lectura del archivo html
    try:
        with open("HTML/index.html", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Archivo HTML no encontrado"

# RUTA PARA AGREGAR LA PELÍCULA
@application.route("/agregar", methods=["POST"])
def agregar_pelicula():
    # RECOGEMOS LOS DATOS DEL FORMULARIO ENVIADO
    codigo = request.form.get("codigo")
    genero = request.form.get("genero")
    edad = request.form.get("edad")
    director = request.form.get("director")
    titulo = request.form.get("titulo")

    # VALIDACIÓN
    if not (codigo or genero or edad or director or titulo):
        return "Error: Todos los campos son requeridos"
    
    # INSERTAMOS EN LA BASE DE DATOS
    conexion = SQLiteConnection("Database1.db")

    conexion.execute_query(
        "INSERT INTO peliculas(codigo, genero, edad, director, titulo) VALUES (?, ?, ?, ?, ?)",
        [codigo, genero, edad, director, titulo],
        commit = True
    )
    

    return "Película agregada correctamente."

if __name__ == "__main__":
    application.run(debug=True)

# RUTA PARA MOSTRAR TODO
@application.route("/mostrar", methods=["GET"])
def mostrar_todo():
    conexion = SQLiteConnection("Database1.db")
    peliculas = conexion.execute_query("SELECT * FROM peliculas")

    return peliculas
