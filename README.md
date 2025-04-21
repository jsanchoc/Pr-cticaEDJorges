# PracticaEDJorges

# INDICE
1. [Comandos para crear la Base de Datos](#baseDatos)
2. [URL](#url)
3. [HTML (index.html)](#html)
    - 3.1 [Datos a tener en cuenta](#html)
4. [Flask Python (código HTML)](#flask)
    - 4.1 [Flask Python (código HTML)](#flask)
    - 4.2 [Función agregar_pelicula](#funcionAgregar)
    - 4.3 [Función mostrar_peliculas](#funcionMostrar)
    - 4.4 [Función eliminar_pelicula](#funcionEliminar)
5. [FUENTES](#fuentes)


# Primeros pasos <!--JORGE CASAS GÓMEZ-->
- ***Configuarar el entorno virutal Windows-> python -m venv env | macOS-> python3 -m venv env***
- ***Activar Entorno Virtual Windows-> call env/scripts/activate | macOS-> source env/bin/activate***
- ***Crear requirements -> con los módulos a instalar***
- ***Instalar módulos -> pip install -r requirements.txt***
- ***Para el correcto funcionamiento de la API: cd src // flask --app app.py --debug run***


## 1. Comandos para crear la Base de Datos <!--JORGE CASAS GÓMEZ--><div id="baseDatos"></div>

```sql
-- Estructura de tablas
CREATE TABLE peliculas (
    codigo INTEGER PRIMARY KEY,
    genero VARCHAR(20),
    edad INTEGER,
    director VARCHAR(20),
    titulo VARCHAR(20)
);


-- Datos por defecto
INSERT INTO peliculas VALUES 
    (1, 'Acción',           15, 'Nolan',        'Inception'),
    (2, 'Drama',            16, 'Coppola',      'El padrino'),
    (3, 'Comedia',          12, 'Allen',        'Manhattan'),
    (4, 'Suspense',         14, 'Fincher',      'Seven'),
    (5, 'Terror',           18, 'Carpenter',    'Halloween'),
    (6, 'Ciencia ficción',  17, 'Kubrick',      '2001'),
    (7, 'Romance',          13, 'Allen',        'Hitch'),
    (8, 'Aventura',         16, 'Scott',        'Gladiator'),
    (9, 'Fantasía',         16, 'Jackson',      'LOTR'),
    (10, 'Animación',       10, 'Spielberg',    'Shrek');


-- Resultados
SELECT * FROM peliculas;
```

## 2. URL <div id="url"></div>
> URL http://127.0.0.1:5000

## 3. HTML (index.html)<div id="html"></div> <!--JORGE CASAS GÓMEZ-->

### 3.1 Datos a tener en cuenta <!--JORGE CASAS GÓMEZ-->
- ***form action="..."***: Define a qué ruta de la API se enviarán los datos.

- ***method="post"***: Especifica que se usarán los datos del formulario con POST.

- Cada ***input*** tiene un **name** que corresponde con las claves que Flask recogerá para acceder al campo en cuestión.

- Importamos el ***request*** para poder acceder a los datos del formulario.

- La carpeta **static** se ha creado para poder mostrar la imagen de fondo de la página del formulario, ya que, si no, me saltaba el ERROR: **404**..


## 4. Flask Python (código HTML)<div id="flask"></div> <!--JORGE CASAS GÓMEZ-->

### 4.1 Función inicio <div id="flask"></div><!--JORGE CASAS GÓMEZ-->

- ***with open("HTML/index.html", encoding = "utf-8") as f:*** abre el archivo html que está en la carpeta **HTML**, llamado **index.html**.

- ***with***: abre archivos de forma segura y controlada(cierre automático).

- ***encoding = "utf-8"***: permite leer los caracteres especiales **(áéíóú o ñ)**.

- ***as f***: guarda el archivo en la variable **f**.

- ***return f.read***: lee todo el contenido del arxchivo f.read(), luego devuelve el html com respuesta al navegador y el Flask lo muestra como si fuera una página web.


### 4.2 Función agregar_pelicula <div id="funcionAgregar"></div> <!--JORGE CASAS GÓMEZ-->

- ***request.form.get("")***: recoge el valor de lo que se encuentra entre las comillas, en este caso, codigo, edad, genero... del formulario.

- ***SQLiteConnection*** y ***conexion.execute_query*** ejecuta la base de datos usando mi clase personalizada.

### 4.3 Función mostrar_peliculas <div id="funcionMostrar"></div> <!--Jorge Sancho-->

Esta ruta permite mostrar todas las películas registradas en la base de datos. Además, se pueden aplicar filtros opcionales mediante parámetros en la URL, como por ejemplo:
- `codigo`
- `genero`
- `edad`
- `director`
- `titulo`

**Ejemplo de uso:** <!--Jorge Sancho-->

> /mostrar?genero=Acción&edad=18

Esto mostrará solo las películas del género "Acción" recomendadas para mayores de 18 años.

---

**¿Qué hace esta ruta por dentro?** <!--Jorge Sancho-->


1. Usa líneas como `request.args.get("codigo")` para recoger los filtros desde la URL. Si por ejemplo accedes a `/mostrar?codigo=5`, con esa línea se obtiene el valor `5`.
2. Va añadiendo condiciones a la consulta SQL dependiendo de los filtros que vayas poniendo. Por ejemplo, si pones solo la edad, buscará solo por la edad.
3. Usa la clase `SQLiteConnection` para conectarse a la base de datos y poder ejecutar la consulta.
4. Muestra los resultados en la plantilla `mostrar.html`.

---

### 4.4 Función eliminar_pelicula <div id="funcionEliminar"></div> <!--Jorge Sancho-->

Esta ruta borra una película concreta. Solo con poner su código en la URL. Ejemplo:

> /eliminar/12

Esto eliminará la película con código `12`.

---

**¿Qué hace esta ruta por dentro?** <!--Jorge Sancho-->

1. El valor `<codigo>` se recoge directamente de la URL como variable.
2. Se ejecuta la consulta `DELETE` usando el código para borrar la película.
3. Se guardan los cambios en la base de datos con `commit=True`.
4. Te redirige automáticamente a la ruta `/mostrar` para ver el listado actualizado.

---

`if __name__ == "__main__" application.run(debug=True)`: Inicia la app Flask, realizandose la carga automática y mensajes de error.


## FUENTES <div id="fuentes"></div>  <!--JORGE CASAS GÓMEZ-->

- https://realpython.com/ (***Documentación oficial Flask***)
- https://flask.palletsprojects.com/en/latest/patterns/wtforms/ (***Flask y formularios***)
- https://flask.palletsprojects.com/en/latest/api/#flask.Request.form (***Para request.form.get()***)
- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files (***Manejo de archivos en Python with open***)
- https://stackoverflow.com/ <!--Jorge Sancho-->
- https://realpython.com/ <!--Jorge Sancho-->
- https://flask.palletsprojects.com/ <!--Jorge Sancho-->




