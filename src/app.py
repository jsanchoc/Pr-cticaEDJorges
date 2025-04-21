# IMPORTACIÓN DE LIBRERÍAS <!--Jorge Casas-->
from flask import Flask, request, render_template, redirect, url_for
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

# RUTA PARA MOSTRAR TODO <!--Jorge Sancho-->
@application.route("/mostrar", methods=["GET"])
def mostrar_peliculas():
    # Recogemos los posibles argumentos
    codigo = request.args.get("codigo")
    genero = request.args.get("genero")
    edad = request.args.get("edad")
    director = request.args.get("director")
    titulo = request.args.get("titulo")

    # Creamos la base de la consulta
    query = "SELECT * FROM peliculas WHERE 1=1"
    valores = []

    if codigo:
        query += " AND codigo = ?"
        valores.append(codigo)
    if genero:
        query += " AND genero = ?"
        valores.append(genero)
    if edad:
        query += " AND edad = ?"
        valores.append(edad)
    if director:
        query += " AND director = ?"
        valores.append(director)
    if titulo:
        query += " AND titulo = ?"
        valores.append(titulo)

    conexion = SQLiteConnection("Database1.db")
    peliculas = conexion.execute_query(query, valores)

    print(f"CONSULTA: {query} - VALORES: {valores}")
    return render_template("mostrar.html", peliculas=peliculas)

@application.route("/eliminar/<int:codigo>", methods=["GET"])
def eliminar_pelicula(codigo):
    conexion = SQLiteConnection("Database1.db")
    conexion.execute_query(
        "DELETE FROM peliculas WHERE codigo = ?",
        [codigo],
        commit=True
    )
    return redirect(url_for("mostrar_peliculas"))


if __name__ == "__main__":
    application.run(debug=True)