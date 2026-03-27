create database db_amazon;

create table db_amazon.clientes(
    cod_cliente int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) unique not null
);

create table db_amazon.telefones(
    cod_tel int auto_increment primary key,
    numero varchar(20) not null,
    ddd varchar(5) not null,
    cod_cliente int not null,
    foreign key(cod_cliente) references db_amazon.clientes(cod_cliente)
);

insert into db_amazon.clientes(nome, email)
    values("Carlos miguel", "carlos@exemplo.com");

select * from db_amazon.clientes;
