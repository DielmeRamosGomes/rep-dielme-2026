create database if not exists db_s901;

create table if not exists clientes(
    id int auto_increment primary key,
    nome varchar(100) not null,
    cidade varchar(100) not null
);






