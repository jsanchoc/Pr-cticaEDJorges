# Pr-cticaEDJorges

## 1. Comandos para crear la Base de Datos

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