create database if not exists db_join;

create table if not exists db_join.produtos(
    id_produto int auto_increment primary key,
    nome varchar(100) not null,
    categoria varchar(100) not null,
    preco decimal(10, 2) not null
);

create table if not exists db_join.vendas(
    id_venda int auto_increment primary key,
    quantidade int not null,
    data_venda date not null,
    id_produto int not null,
    foreign key(id_produto) references db_join.produtos(id_produto)
);

insert into db_join.produtos(nome, categoria, preco)
    values("computador", "Eletrônicos", 3500),
          ("Cadeira", "Móveis", 200),
          ("Cama", "Móveis", 1000),
          ("Tênis", "Calçados", 3000),
          ("Mesa Gamer", "Eletrônicos", 1500);

select * from db_join.produtos;

insert into db_join.vendas(quantidade, data_venda, id_produto)
    values(2, "2026-04-14", 1),
          (3, "2026-04-15", 2),
          (4, "2026-03-15", 3),
          (5, "2026-03-16", 4),
          (6, "2026-05-13", 5),
          (7, "2026-05-13", 1);

select * from db_join.vendas;

-- 1.Qual foi o produto mais vendido nos últimos três meses?

select p.nome, count(v.id_produto) as produto_mais_vendido 
    from db_join.produtos as p join db_join.vendas as v
        on p.id_produto = v.id_produto 
            where v.data_venda >= date_sub(curdate(), interval 3 month)
                group by p.nome 
                    order by produto_mais_vendido desc 
                        limit 1;

-- 2.Qual foi o valor total de vendas por categoria no mês passado?

select 
    p.categoria, sum(p.preco * v.quantidade) as valor_total_por_categoria
from db_join.produtos as p join db_join.vendas as v
on p.id_produto = v.id_produto
where v.data_venda >= date_sub(curdate(), interval 1 month)
group by p.categoria 
order by valor_total_por_categoria desc;

-- 3.Qual foi a média de produtos vendidos nos últimos três meses?

select 
    avg(soma_total_produtos) as media_produtos from 
    (select 
        sum(p.preco * v.quantidade) as soma_total_produtos 
        from db_join.produtos as p join db_join.vendas as v
        on p.id_produto = v.id_produto 
        where v.data_venda 
        between "2026-03-01" and curdate()
    ) as soma;


-- 4.Qual foi o valor da venda mais alta e da mais baixa nos últimos três meses?
SELECT 
    MAX(p.preco * v.quantidade) AS venda_mais_alta,
    MIN(p.preco * v.quantidade) AS venda_mais_baixa
FROM db_join.produtos AS p
JOIN db_join.vendas AS v ON p.id_produto = v.id_produto
WHERE v.data_venda >= "2026-03-01";