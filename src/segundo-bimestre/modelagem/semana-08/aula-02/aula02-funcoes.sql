create database db_dielmeloja;

create table db_dielmeloja.vendas(
    id_venda int auto_increment primary key,
    produto varchar(100) not null,
    quantidade int not null,
    valor_unitario decimal(10, 2) not null,
    data_venda date not null
);

insert into db_dielmeloja.vendas(produto, quantidade, valor_unitario, data_venda) 
    values("computador", 2, 3000, "2026-04-10"),
    ("mesa gamer", 3, 2000, "2026-04-11");

insert into db_dielmeloja.vendas(produto, quantidade, valor_unitario, data_venda) 
    values("Fone Gamer", 3, 100, "2026-04-11"),
    ("Mouse gamer", 4, 500, "2026-04-13"),
    ("TV Gamer", 1, 5000, "2026-04-15");

select * from db_dielmeloja.vendas;

select v.id_venda, v.produto, v.quantidade from db_dielmeloja.vendas as v;  

--1.Quantas vendas foram realizadas no mês passado?
SELECT COUNT(*) AS total_vendas
    FROM db_dielmeloja.vendas as v
        WHERE v.data_venda 
            BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) 
                AND LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

--2.Qual foi o valor total de vendas de cada produto?

SELECT v.produto, SUM(v.quantidade * v.valor_unitario) AS valor_total
    FROM db_dielmeloja.vendas as v 
        GROUP BY v.produto;

--3.Qual foi o produto mais vendido em quantidade?

select v.produto, max(quantidade) as maior_quantidade
    from db_dielmeloja.vendas as v 
        group by v.quantidade desc limit 1;

-- 4.Qual foi o valor médio das vendas por dia no mês passado?

select avg(faturamento_diario) as media_de_vendas
    from (
        select sum(v.quantidade * v.valor_unitario) as faturamento_diario
            from db_dielmeloja.vendas as v
                where v.data_venda 
                    between date_sub(curdate(), interval 1 month)
                        and last_day(date_sub(curdate(), interval 1 month))
                           group by v.data_venda) as resumo_mensal;





