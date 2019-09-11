/*Database creëren*/
CREATE DATABASE kastje;
/*Gebruiker aanmaken*/
CREATE USER 'backend-service'@'localhost' IDENTIFIED BY 'geheim!';
/*Permissies geven aan reeds aangemaakte gebruiker*/
GRANT ALL PRIVILEGES ON kastje.* TO 'backend-service'@'localhost';
USE kastje;
/*Table creëren*/
CREATE TABLE IF NOT EXISTS history (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,tijd DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
/*Correct table*/
CREATE TABLE kastje.history ( id INT(22) NOT NULL AUTO_INCREMENT , tijd TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (id));
