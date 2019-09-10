/*Database creëren*/
CREATE DATABASE kastje;
/*Gebruiker aanmaken*/
CREATE USER 'backend-service'@'localhost' IDENTIFIED BY 'geheim!';
/*Permissies geven aan reeds aangemaakte gebruiker*/
GRANT ALL ON kastje.* TO 'backend-service'@'localhost';
USE kastje;
/*Table creëren*/
CREATE TABLE IF NOT EXISTS history (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,tijd DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
