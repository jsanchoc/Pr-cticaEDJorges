# IMPORTACION DE LIBRERIAS
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection

# CONFIGURACION DEL PROYECTO
application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

# PAGINAS PARA QUE ME APAREZCA UNA PAG INICIO
@application.route("/", methods=("GET","POST"))
def inicio():
    return "Página de inicio"

@application.route("/peliculas")
def conexion():
    conexion = SQLiteConnection("Database1.db")
    peliculas = conexion.execute_query("SELECT * FROM peliculas")
    return peliculas

