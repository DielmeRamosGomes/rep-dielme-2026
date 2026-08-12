create database if not exists db_s16a1;

create table if not exists db_s16a1.clientes(
    id_cliente int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null,
    telefone varchar(100) not null 
)Engine=InnoDB;

create table if not exists db_s16a1.pedidos(
    id_pedido int primary key auto_increment,
    data_pedido date not null,
    valor_total decimal(10, 2) not null,
    id_cliente int not null,
    constraint fk_cliente_pedido foreign key(id_cliente) references db_s16a1.clientes(id_cliente) 
    on delete cascade on update cascade
)Engine=InnoDB;

insert into db_s16a1.clientes(nome, email, telefone)
values("Lucas Lorenzo", "lucas@exemplo.com", "11-98343-2324");

