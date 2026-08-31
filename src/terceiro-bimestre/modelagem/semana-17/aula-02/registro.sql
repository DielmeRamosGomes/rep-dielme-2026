CREATE DATABASE IF NOT EXISTS loja;

USE loja;

CREATE TABLE loja.clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_cadastro DATE NOT NULL
);
CREATE TABLE loja.compras (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    data_compra DATE NOT NULL
);

INSERT INTO loja.clientes (nome, email, data_cadastro) VALUES
('João Silva', 'joao.silva@example.com', '2023-01-15'),
('Maria Oliveira', 'maria.oliveira@example.com', '2023-02-20');

INSERT INTO loja.compras (cliente_id, valor_total, data_compra) VALUES
(1, 150.00, '2024-09-05'),
(2, 200.00, '2024-09-10'),
(1, 75.50, '2024-09-15'),
(2, 300.00, '2024-09-20'),
(1, 50.00, '2024-09-25');


-- ============================================================
-- Questão 1: Calcule o valor total das vendas realizadas até hoje.
-- Utiliza a função SUM para somar o valor de todas as compras na tabela compras.
-- ============================================================
SELECT SUM(valor_total) AS total_vendas
FROM loja.compras;


-- ============================================================
-- Questão 2: Quantos clientes únicos fizeram compras no sistema?
-- Utiliza a função COUNT com DISTINCT para contar a quantidade de clientes distintos na tabela compras.
-- ============================================================
SELECT COUNT(DISTINCT cliente_id) AS total_clientes_unicos
FROM loja.compras;


-- ============================================================
-- Questão 3: Qual é o valor médio gasto por compra?
-- Utiliza a função AVG para calcular o valor médio gasto por compra em todas as transações da tabela compras.
-- ============================================================
SELECT AVG(valor_total) AS valor_medio_por_compra
FROM loja.compras;


-- ============================================================
-- Questão 4: Quantas compras foram feitas em um determinado mês?
-- (Exemplo: Setembro de 2024)
-- Utiliza a função COUNT e a cláusula WHERE com funções de data (YEAR e MONTH) para filtrar o período.
-- ============================================================
SELECT COUNT(*) AS total_compras_mes
FROM loja.compras
WHERE YEAR(data_compra) = 2024 AND MONTH(data_compra) = 9;

-- Alternativa para filtragem por intervalo de datas no mês de setembro/2024:

SELECT COUNT(*) AS total_compras_mes
FROM loja.compras
WHERE data_compra BETWEEN '2024-09-01' AND '2024-09-30';
