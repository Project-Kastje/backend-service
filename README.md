# backend-service

Dit script registreert als er een beweging en:

- zet het in de database
- geeft een signaal aan de web service

## TODO iemand sql script van maken????::::
```bash
pi@reapermini:~/src/pk/backend-service $ sudo mariadb 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 236
Server version: 10.1.38-MariaDB-0+deb9u1 Raspbian 9.0

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE kastje
    -> ;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> CREATE USER 'backend-service'@'localhost' IDENTIFIED BY 'geheim!'
    -> ;
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> GRANT SELECT ON kastje TO 'backend-service'@'localhost';
ERROR 1046 (3D000): No database selected
MariaDB [(none)]> GRANT SELECT ON kastje.* TO 'backend-service'@'localhost';
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> USE kastje;
Database changed
MariaDB [kastje]> CREATE TABLE IF NOT EXISTS history (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, tijd TIMESTAMP);
Query OK, 0 rows affected (0.10 sec)
```
