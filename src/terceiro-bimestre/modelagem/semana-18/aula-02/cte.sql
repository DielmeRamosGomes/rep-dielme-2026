CREATE DATABASE IF NOT EXISTS s18a2;


CREATE TABLE IF NOT EXISTS s18a2.funcionarios(
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    id_supervisor INT NULL,
    FOREIGN KEY (id_supervisor) REFERENCES s18a2.funcionarios(id_funcionario)
);

CREATE TABLE IF NOT EXISTS s18a2.vendas(
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    id_funcionario INT NOT NULL,
    valor_venda DECIMAL(10, 2) NOT NULL,
    data_venda DATE NOT NULL,
    FOREIGN KEY (id_funcionario) REFERENCES s18a2.funcionarios(id_funcionario)
);

INSERT INTO s18a2.funcionarios (nome, id_supervisor) 
VALUES ('João Silva', NULL),
       ('Maria Oliveira', 1),
       ('Carlos Souza', 1),
       ('Ana Costa', 2),
       ('Pedro Lima', 2);

SELECT * FROM s18a2.funcionarios;

INSERT INTO s18a2.vendas(id_funcionario, valor_venda, data_venda)
VALUES(2, 1500.00, '2026-08-01'),
(3, 2000.00, '2026-08-02'),
(4, 2500.00, '2026-08-03'),
(5, 3000.00, '2026-08-04'),
(2, 1800.00, '2026-09-05'),
(3, 2200.00, '2026-09-06'),
(4, 2700.00, '2026-09-07'),
(5, 3200.00, '2026-09-08');

SELECT * FROM s18a2.vendas;

-- 3) Criem uma consulta usando WITH para calcular o total de 
-- vendas de todos os funcionários. A consulta deve retornar o 
-- nome do funcionário e o total de suas vendas.

WITH TotalVendas AS (
    SELECT id_funcionario, SUM(valor_venda) AS total_vendas
    FROM s18a2.vendas
    GROUP BY id_funcionario
)
SELECT f.nome, tv.total_vendas
FROM s18a2.funcionarios f
LEFT JOIN TotalVendas tv ON f.id_funcionario = tv.id_funcionario;

-- 4)Criem uma CTE recursiva para listar todos os funcionários
--e seus supervisores diretos, mostrando a hierarquia de cada 
--funcionário. Isso ajudará a visualizar a relação hierárquica 
--dentro da empresa.

WITH RECURSIVE hierarquia_funcionarios AS (
    SELECT id_funcionario, nome, id_supervisor, 1 AS nivel
    FROM s18a2.funcionarios
    WHERE id_supervisor IS NULL
    UNION ALL
    SELECT f.id_funcionario, f.nome, f.id_supervisor, hf.nivel + 1
    FROM s18a2.funcionarios f
    JOIN hierarquia_funcionarios hf ON f.id_supervisor = hf.id_funcionario
)
SELECT * FROM hierarquia_funcionarios;

-- 5) Com base na CTE recursiva criada, criem uma nova consulta que calcule 
-- o total de vendas de cada funcionário e de sua equipe (incluindo vendas de 
-- seus subordinados diretos e indiretos).

WITH RECURSIVE ArvoreHierarquica AS (
    -- Caso base: Cada funcionário é considerado "ancestral" de si mesmo
    SELECT 
        id_funcionario AS id_lider, 
        id_funcionario AS id_subordinado
    FROM s18a2.funcionarios
    UNION ALL
    -- Passo recursivo: Conecta os líderes aos subordinados diretos e indiretos
    SELECT 
        ah.id_lider, 
        f.id_funcionario AS id_subordinado
    FROM ArvoreHierarquica ah
    INNER JOIN s18a2.funcionarios f ON f.id_supervisor = ah.id_subordinado
),
VendasIndividuais AS (
    -- Agrupa as vendas próprias de cada funcionário
    SELECT 
        id_funcionario, 
        SUM(valor_venda) AS valor_proprio
    FROM s18a2.vendas
    GROUP BY id_funcionario
)
-- Consulta final: Calcula vendas próprias, da equipe e o total consolidado
SELECT 
    f.nome AS funcionario,
    COALESCE(vi.valor_proprio, 0.00) AS vendas_proprias,
    COALESCE(SUM(v_sub.valor_venda), 0.00) AS vendas_equipe_total
FROM s18a2.funcionarios f
LEFT JOIN VendasIndividuais vi ON f.id_funcionario = vi.id_funcionario
LEFT JOIN ArvoreHierarquica ah ON f.id_funcionario = ah.id_lider
LEFT JOIN s18a2.vendas v_sub ON ah.id_subordinado = v_sub.id_funcionario
GROUP BY f.id_funcionario, f.nome, vi.valor_proprio
ORDER BY f.id_funcionario;




