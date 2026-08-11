create database db_tech;

create table if not exists db_tech.Clientes(
    id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null unique
);

create table if not exists db_tech.Fornecedor(
    id int primary key auto_increment,
    rua varchar(200) not null,
    numero varchar(100) not null
);

alter table db_tech.Fornecedor add column
nome varchar(100) not null;

alter table db_tech.Fornecedor add column
contato varchar(100) not null;


create table if not exists db_tech.Produtos(
    id int primary key auto_increment,
    nome varchar(100) not null,
    preco decimal(10, 2) not null,
    id_fornecedor int not null,
    foreign key(id_fornecedor) references db_tech.Fornecedor(id)
);

create table if not exists db_tech.Pedidos(
    id int primary key auto_increment,
    cliente_id int not null,
    data_pedido date not null,
    foreign key(cliente_id) references db_tech.Clientes(id)
);

create table if not exists db_tech.Itens_Pedido(
    id int primary key auto_increment,
    pedido_id int not null,
    produto_id int not null,
    foreign key(pedido_id) references db_tech.Pedidos(id),
    foreign key(produto_id) references db_tech.Produtos(id)   
);

insert into db_tech.Clientes(nome, email)
values("João Silva", "joao@exemplo.com"),
      ("Maria Oliveira", "maria@exemplo.com"),
      ("Pedro Santos", "pedro@exemplo.com");

select * from db_tech.Clientes;

insert into db_tech.Fornecedor(rua, numero)
    values("Rua A", "1234"),
          ("Rua B", "5678");

insert into db_tech.Fornecedor(rua, numero, nome, contato)
    values("Av. das Indústrias", "500", "GlobalTech", "contato@globaltech.com");

update db_tech.Fornecedor as f set f.nome = "Nickolas"
    where f.id = 1;

update db_tech.Fornecedor as f set f.nome = "Nathan"
    where f.id = 2;

delete from db_tech.Fornecedor 
where db_tech.Fornecedor.id = 2;

select * from db_tech.Fornecedor;

insert into db_tech.Produtos(nome, preco, id_fornecedor)
values("Camiseta", 29.99, 1),
      ("Calça Jeans", 79.99, 1),
      ("Tênis", 149.99, 2),
      ("Jaqueta", 199.99, 2);

select * from db_tech.Produtos;

insert into db_tech.Pedidos(cliente_id, data_pedido)
values(1, "2026-05-15"),
      (2, "2026-05-20"),
      (1, "2026-05-25"),
      (3, "2026-05-27");

alter table db_tech.Itens_Pedido add column quantidade int not null;

insert into db_tech.Itens_Pedido(pedido_id, produto_id, quantidade)
values(1, 1, 2),
      (1, 2, 3),
      (2, 3, 4),
      (2, 4, 5),
      (3, 1, 1),
      (3, 3, 2);

select c.nome as cliente, p.nome as produto, ip.quantidade
from db_tech.Clientes c
join db_tech.Pedidos pe on c.id = pe.cliente_id
join db_tech.Itens_Pedido ip on pe.id = ip.pedido_id
join db_tech.Produtos p on ip.produto_id = p.id
where c.nome = 'João Silva'
order by p.nome;

update db_tech.Produtos
set nome = 'Calça de Couro'
where nome = 'Calça Jeans';

select * from db_tech.Produtos;

select sum(p.preco * ip.quantidade) as total_vendas
from db_tech.Pedidos pe
join db_tech.Itens_Pedido ip on pe.id = ip.pedido_id
join db_tech.Produtos p on ip.produto_id = p.id;

select count(*) as total_pedidos
from db_tech.Pedidos pe
join db_tech.Clientes c on pe.cliente_id = c.id
where c.nome = 'João Silva';