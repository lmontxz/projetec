CREATE DATABASE af;
use af;

CREATE TABLE login (
    id INT AUTO_INCREMENT primary key,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR (255) NOT NULL
);

SELECT * FROM login;


