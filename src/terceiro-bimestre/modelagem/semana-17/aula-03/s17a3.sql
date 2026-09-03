create database if not exists db_s17a3;

create table if not exists db_s17a3.clientes(
    cliente_id int auto_increment PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE 
);

create table if not exists db_s17a3.compras(
    compra_id int auto_increment PRIMARY KEY,
    cliente_id int NOT NULL,
    valor_total decimal(10, 2) NOT NULL,
    data_compra date NOT NULL  
);

INSERT INTO db_s17a3.clientes(nome, email) 
VALUES("Carlos", "carlos@exemplo.com"),
      ("Roberto", "roberto@exemplo.com"),
      ("Ana", "ana@exemplo.com");

SELECT * FROM db_s17a3.clientes;

INSERT INTO db_s17a3.compras(cliente_id, valor_total, data_compra)
VALUES(1, 4000.0, "2026-09-01"),
      (1, 3000.0, "2026-08-31"),
      (2, 2000.0, "2026-09-01"),
      (2, 1000.0, "2026-08-31");
      
SELECT * FROM db_s17a3.compras;

-- 1) exibir uma lista com o nome do cliente, o e-mail, e o 
-- valor total de cada compra realizada. Nessa consulta, 
-- apenas os clientes que têm compras registradas devem ser 
-- exibidos.

create view if not exists db_s17a3.mostra_compra_do_cliente AS
SELECT c.nome, c.email, co.valor_total 
FROM db_s17a3.clientes c
JOIN db_s17a3.compras co on c.cliente_id = co.cliente_id
ORDER BY c.nome;

SELECT * FROM db_s17a3.mostra_compra_do_cliente;

create view if not exists db_s17a3.mostra_compra_do_cliente_valor AS
SELECT c.nome, c.email, co.valor_total 
FROM db_s17a3.clientes c
JOIN db_s17a3.compras co on c.cliente_id = co.cliente_id
ORDER BY co.valor_total;

SELECT * FROM db_s17a3.mostra_compra_do_cliente_valor;

-- 2) 

create view if not exists db_s17a3.mostra_compra_do_cliente_left AS
SELECT c.nome, c.email, co.valor_total 
FROM db_s17a3.clientes c
left JOIN db_s17a3.compras co on c.cliente_id = co.cliente_id
ORDER BY c.nome;


