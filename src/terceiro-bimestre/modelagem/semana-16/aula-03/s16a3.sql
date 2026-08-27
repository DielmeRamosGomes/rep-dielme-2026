create database if not exists db_s16a3;

CREATE TABLE if not exists db_s16a3.pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100),
    produto VARCHAR(100),
    quantidade INT,
    valor DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'Pendente'
);

insert into db_s16a3.pedidos(cliente, produto, quantidade, valor)
values("Carlito Tevez", "Chuteira", 2, 100.0);

SELECT * FROM db_s16a3.pedidos;

START TRANSACTION;

INSERT INTO db_s16a3.pedidos (cliente, produto, quantidade, valor) 
VALUES ('João Silva', 'Notebook', 1, 3500.00);

-- Simular um erro ou decisão de desfazer a transação
ROLLBACK;

START TRANSACTION;

INSERT INTO db_s16a3.pedidos (cliente, produto, quantidade, valor) 
VALUES ('Maria Souza', 'Smartphone', 2, 2000.00);

COMMIT;

START TRANSACTION;

INSERT INTO db_s16a3.pedidos (cliente, produto, quantidade, valor) 
VALUES ('Carlos Lima', 'Tablet', 1, 1500.00);

-- Simular erro que exige ROLLBACK
-- Por exemplo: tentativa de inserir um valor 
-- inconsistente
INSERT INTO db_s16a3.pedidos (cliente, produto, quantidade, valor) 
VALUES (NULL, 'Smartwatch', -1, 500.00);  -- Dados inválidos

ROLLBACK;




