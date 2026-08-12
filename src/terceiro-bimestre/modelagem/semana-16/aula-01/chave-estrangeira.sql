create database if not exists db_kabum;

create table if not exists db_kabum.clientes(
    id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null unique
)Engine=InnoDB;

create table if not exists db_kabum.pedidos(
    id int primary key auto_increment,
    id_cliente int not null,
    data_pedido date not null,
    constraint fk_id_cliente foreign key (id_cliente) references db_kabum.clientes(id_cliente) 
    on delete cascade on update cascade
) Engine=InnoDB;

insert into db_kabum.clientes(nome, email) values
("João Silva", "joao@exemplo.com");

insert into db_kabum.pedidos(id_cliente, data_pedido) values
(1, "2026-08-10");

delete from db_kabum.clientes where id = 1;

select * from db_kabum.clientes;
select * from db_kabum.pedidos;

