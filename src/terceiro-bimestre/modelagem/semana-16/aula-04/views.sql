CREATE DATABASE IF NOT EXISTS db_vendas;

USE db_vendas;

CREATE TABLE IF NOT EXISTS db_vendas.clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS db_vendas.produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  preco DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS db_vendas.vendas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_cliente INT NOT NULL,
  id_produto INT NOT NULL,
  data_venda DATE NOT NULL,
  quantidade INT NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES db_vendas.clientes(id),
  FOREIGN KEY (id_produto) REFERENCES db_vendas.produtos(id)
);

INSERT INTO db_vendas.clientes (nome, email) VALUES
('João Silva', 'joao@email.com'),
('Maria Oliveira', 'maria@email.com');

select * from db_vendas.clientes;

INSERT INTO db_vendas.produtos(nome, preco) 
VALUES ('Produto A', 10.00),
       ('Produto B', 20.00);


INSERT INTO db_vendas.vendas (id_cliente, id_produto, data_venda, quantidade)
VALUES (1, 1, '2026-08-27', 2),
       (1, 2, '2026-08-26', 1),
       (2, 1, '2026-08-25', 3);

CREATE VIEW relatorio_vendas AS
SELECT 
  c.nome AS cliente, 
  p.nome AS produto, 
  v.data_venda, 
  v.quantidade
FROM db_vendas.vendas v
JOIN db_vendas.clientes c ON v.id_cliente = c.id
JOIN db_vendas.produtos p ON v.id_produto = p.id;

SELECT * FROM relatorio_vendas;