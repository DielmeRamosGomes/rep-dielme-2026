create database db_loja_online;

create table if not exists db_loja_online.Clientes(
    id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null unique
);

create table if not exists db_loja_online.Produtos(
    id int primary key auto_increment,
    nome varchar(100) not null,
    preco decimal(10, 2) not null
);

create table if not exists db_loja_online.Pedidos(
    id int primary key auto_increment,
    cliente_id int not null,
    data_pedido date not null,
    foreign key(cliente_id) references db_loja_online.Clientes(id)
);

create table if not exists db_loja_online.Itens_Pedido(
    id int primary key auto_increment,
    pedido_id int not null,
    produto_id int not null,
    foreign key(pedido_id) references db_loja_online.Pedidos(id),
    foreign key(produto_id) references db_loja_online.Produtos(id)   
);

insert into db_loja_online.Clientes(nome, email)
values("João Silva", "joao@exemplo.com"),
      ("Maria Oliveira", "maria@exemplo.com"),
      ("Pedro Santos", "pedro@exemplo.com");

select * from db_loja_online.Clientes;

insert into db_loja_online.Produtos(nome, preco)
values("Camiseta", 29.99),
      ("Calça Jeans", 79.99),
      ("Tênis", 149.99),
      ("Jaqueta", 199.99);

select * from db_loja_online.Produtos;

insert into db_loja_online.Pedidos(cliente_id, data_pedido)
values(1, "2026-05-15"),
      (2, "2026-05-20"),
      (1, "2026-05-25"),
      (3, "2026-05-27");

alter table db_loja_online.Itens_Pedido add column quantidade int not null;

insert into db_loja_online.Itens_Pedido(pedido_id, produto_id, quantidade)
values(1, 1, 2),
      (1, 2, 3),
      (2, 3, 4),
      (2, 4, 5),
      (3, 1, 1),
      (3, 3, 2);

select c.nome as cliente, p.nome as produto, ip.quantidade
from db_loja_online.Clientes c
join db_loja_online.Pedidos pe on c.id = pe.cliente_id
join db_loja_online.Itens_Pedido ip on pe.id = ip.pedido_id
join db_loja_online.Produtos p on ip.produto_id = p.id
where c.nome = 'João Silva'
order by p.nome;

update db_loja_online.Produtos
set nome = 'Calça de Couro'
where nome = 'Calça Jeans';

select * from db_loja_online.Produtos;

select sum(p.preco * ip.quantidade) as total_vendas
from db_loja_online.Pedidos pe
join db_loja_online.Itens_Pedido ip on pe.id = ip.pedido_id
join db_loja_online.Produtos p on ip.produto_id = p.id;

select count(*) as total_pedidos
from db_loja_online.Pedidos pe
join db_loja_online.Clientes c on pe.cliente_id = c.id
where c.nome = 'João Silva';