DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes(
    id_cliente INTEGER PRIMARY KEY  AUTOINCREMENT,
    nombre     VARCHAR(50) NOT NULL,
    email      VARCHAR(50) NOT NULL
    );

INSERT INTO clientes (nombre,email) VALUES
("Addair","addair@email.com"),
("Miguel","miguel@email.com"),
("Jose","jose@email.com");

.headers ON

SELECT * FROM clientes;
