create database if not exists db_s17a4;

create table if not exists db_s17a4.clientes(
    cliente_id int auto_increment PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE 
);

create table if not exists db_s17a4.compras(
    compra_id int auto_increment PRIMARY KEY,
    cliente_id int NOT NULL,
    valor_total decimal(10, 2) NOT NULL,
    data_compra date NOT NULL  
);

INSERT INTO db_s17a4.clientes(nome, email) 
VALUES("Carlos", "carlos@exemplo.com"),
      ("Roberto", "roberto@exemplo.com"),
      ("Ana", "ana@exemplo.com");

SELECT * FROM db_s17a4.clientes;

INSERT INTO db_s17a4.compras(cliente_id, valor_total, data_compra)
VALUES(1, 4000.0, "2026-09-01"),
      (1, 3000.0, "2026-08-31"),
      (2, 2000.0, "2026-09-01"),
      (2, 1000.0, "2026-08-31");
      
SELECT * FROM db_s17a4.compras;

-- 1) Qual o total de compras por cliente?

SELECT c.nome,
    (
        SELECT COUNT(*) 
        FROM db_s17a4.compras co 
        WHERE co.cliente_id = c.cliente_id
    ) AS total_compras
FROM db_s17a4.clientes c;

-- 2) Quais clientes gastaram acima da média?

SELECT DISTINCT c.cliente_id, c.nome, c.email
FROM db_s17a4.clientes c
JOIN db_s17a4.compras co ON c.cliente_id = co.cliente_id
WHERE 
    co.valor_total > (
        SELECT AVG(valor_total) 
        FROM db_s17a4.compras
    );

