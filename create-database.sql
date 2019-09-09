/*Database creëren*/
CREATE DATABASE kastje;
/*Gebruiker aanmaken*/
CREATE USER 'backend-service'@'localhost' IDENTIFIED BY 'geheim!';
/*Permissies geven aan reeds aangemaakte gebruiker*/
GRANT SELECT ON kastje.* TO 'backend-service'@'localhost';
GRANT INSERT on kastje.* TO 'backend-service'@'localhost';
USE kastje;
/*Table creëren*/
CREATE TABLE IF NOT EXISTS history (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,DATATIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
