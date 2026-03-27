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

insert into db_amazon.telefones(numero, ddd, cod_cliente)
    values("98834-7648", "12", 1);

insert into db_amazon.telefones(numero, ddd, cod_cliente)
    values("98834-7612", "11", 1);

insert into db_amazon.clientes(nome, email)
    values("Roberto Carlos", "roberto@exemplo.com");

insert into db_amazon.telefones(numero, ddd, cod_cliente)
    values("98834-1212", "13", 2);

insert into db_amazon.telefones(numero, ddd, cod_cliente)
    values("98834-1415", "10", 2);

select * from db_amazon.clientes;

select * from db_amazon.telefones;

select c.nome, t.ddd, t.numero from 
    db_amazon.clientes as c, 
        db_amazon.telefones as t where
            c.cod_cliente = t.cod_cliente;


