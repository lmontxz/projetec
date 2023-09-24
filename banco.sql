create database teste;
use teste;

   CREATE TABLE IF NOT EXISTS clientes (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(255) NOT NULL,
       email VARCHAR(255) NOT NULL,
       senha VARCHAR(255) NOT NULL
   );
   
   select * from clientes;
