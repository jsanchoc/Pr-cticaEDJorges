# PracticaEDJorges

# Primeros pasos <!--JORGE CASAS GÓMEZ-->
- ***Configuarar el entorno virutal -> python -m venv env***
- ***Activar Entorno Virtual -> call env/scripts/activate***
- ***Crear requirements -> con los módulos a instalar***
- ***Instalar módulos -> pip install -r requirements.txt***
- ***Para el correcto funcionamiento de la API: cd src// flask --app app.py --debug run***


## 1. Comandos para crear la Base de Datos <!--JORGE CASAS GÓMEZ-->

```
CREATE TABLE peliculas(
codigo INTEGER PRIMARY KEY,
genero VARCHAR(20),
edad INTEGER,
director VARCHAR(20),
titulo VARCHAR(20)
);


INSERT INTO peliculas VALUES(1, 'Acción', 15, 'Nolan', 'Inception');
INSERT INTO peliculas VALUES(2, 'Drama', 16, 'Coppola', 'El padrino');
INSERT INTO peliculas VALUES(3, 'Comedia', 12, 'Allen', 'Manhattan');
INSERT INTO peliculas VALUES(4, 'Suspense', 14, 'Fincher', 'Seven');
INSERT INTO peliculas VALUES(5, 'Terror', 18, 'Carpenter', 'Halloween');
INSERT INTO peliculas VALUES(6, 'Ciencia ficción', 17, 'Kubrick', '2001');
INSERT INTO peliculas VALUES(7, 'Romance', 13, 'Allen', 'Hitch');
INSERT INTO peliculas VALUES(8, 'Aventura', 16, 'Scott', 'Gladiator');
INSERT INTO peliculas VALUES(9, 'Fantasía', 16, 'Jackson', 'LOTR');
INSERT INTO peliculas VALUES(10, 'Animación', 10, 'Spielberg', 'Shrek');
```
## 2. URL 
> URL http://127.0.0.1:5000

## 3. HTML (index.html) <!--JORGE CASAS GÓMEZ-->

### 3.1 Datos a tener en cuenta <!--JORGE CASAS GÓMEZ-->
- ***form action="..."***: Define a qué ruta de la API se enviarán los datos.

- ***method="post"***: Especifica que se usarán los datos del formulario con POST.

- Cada ***input*** tiene un **name** que corresponde con las claves que Flask recogerá para acceder al campo en cuestión.

- Importamos el ***request*** para poder acceder a los datos del formulario.


## 4. Flask Python (código HTML) <!--JORGE CASAS GÓMEZ-->

### 4.1 Función inicio <!--JORGE CASAS GÓMEZ-->

- ***with open("HTML/index.html", encoding = "utf-8") as f:*** abre el archivo html que está en la carpeta **HTML**, llamado **index.html**.

- ***with***: abre archivos de forma segura y controlada(cierre automático).

- ***encoding = "utf-8"***: permite leer los caracteres especiales **(áéíóú o ñ)**.

- ***as f***: guarda el archivo en la variable **f**.

- ***return f.read***: lee todo el contenido del arxchivo f.read(), luego devuelve el html com respuesta al navegador y el Flask lo muestra como si fuera una página web.


### 4.2 Función agregar_pelicula <!--JORGE CASAS GÓMEZ-->

- ***request.form.get("")***: recoge el valor de lo que se encuentra entre las comillas, en este caso, codigo, edad, genero... del formulario.

- ***SQLiteConnection*** y ***conexion.execute_query*** ejecuta la base de datos usando mi clase personalizada.

- ***if __name__ == "__main__"
    application.run(debug=True)***: Inicia la app Flask, realizandose la carga automática y mensajes de error.


## FUENTES <!--JORGE CASAS GÓMEZ-->

- https://realpython.com/ (***Documentación oficial Flask***)
- https://flask.palletsprojects.com/en/latest/patterns/wtforms/ (***Flask y formularios***)
- https://flask.palletsprojects.com/en/latest/api/#flask.Request.form (***Para request.form.get()***)
- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files (***Manejo de archivos en Python with open***)



