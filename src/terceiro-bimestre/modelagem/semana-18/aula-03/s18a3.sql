create database if not exists s18a3;

CREATE TABLE s18a3.clientes(
    id int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE s18a3.fornecedores(
    id int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO  s18a3.clientes(nome, cidade, email) 
VALUES("João Silva", "São Paulo", "joao@email.com"),
("Maria Santos", "Rio de Janeiro", "maria@email.com"),
("Pedro Lima", "São Paulo", "pedro@email.com");

INSERT INTO  s18a3.fornecedores(nome, cidade, email) 
VALUES("João Silva", "São Paulo", "joao@fornece.com"),
("Ana Costa", "Salvador", "ana@fornece.com"),
("Carlos Nunes", "Recife", "carlos@fornece.com");

-- 1) 
SELECT nome, cidade FROM s18a3.clientes
UNION
SELECT nome, cidade  FROM s18a3.fornecedores;

-- 2) 
SELECT nome FROM s18a3.clientes
UNION ALL
SELECT nome FROM s18a3.fornecedores;

--3) 
SELECT nome, email FROM s18a3.clientes
UNION ALL
SELECT nome, email FROM s18a3.fornecedores;

--4)
SELECT nome, COUNT(*) AS total
FROM (
    SELECT c.nome FROM s18a3.clientes c
    UNION ALL
    SELECT f.nome FROM s18a3.fornecedores f
) AS nomes_combinados
GROUP BY nome
HAVING COUNT(*) > 1;

