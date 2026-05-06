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





