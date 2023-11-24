CREATE DATABASE af;
use af;

CREATE TABLE login (
    id INT AUTO_INCREMENT primary key,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR (255) NOT NULL
);

CREATE TABLE consulta (
    id INT AUTO_INCREMENT primary key,
    data date NOT NULL,
    inicio time NOT NULL,
    termino time NOT NULL,
    descricao VARCHAR(255)
);

SELECT * FROM login;



