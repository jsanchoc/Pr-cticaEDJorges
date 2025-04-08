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