create database db_semana08;

create table db_semana08.Clientes(
    cliente_id int auto_increment primary key,
    nome varchar(100) not null,
    idade int not null,
    email varchar(100) not null,
    senha varchar(100) not null 
);

insert into db_semana08.Clientes(nome, idade, email, senha)
    values("Dielme", 32, "dielme@exemplo.com", "dielme123"),
          ("Carlos", 28, "carlos@exemplo.com", "carlos123"),
          ("Roberto", 35, "roberto@exemplo.com", "roberto123");

select * from db_semana08.Clientes 
    where cliente_id = 1;

select * from db_semana08.Clientes 
    where email = "roberto@exemplo.com";

select * from db_semana08.Clientes order by nome asc;

select * from db_semana08.Clientes order by nome desc;

select * from db_semana08.Clientes order by email asc;