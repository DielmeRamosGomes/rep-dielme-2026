create database db_semana08;

create table db_semana08.Clientes(
    cliente_id int auto_increment primary key,
    nome varchar(100) not null,
    idade int not null,
    email varchar(100) not null,
    senha varchar(100) not null 
);

insert into db_semana08.Clientes(email, senha, nome)
    values("dielme@exemplo.com", "dielme123", "Dielme"),
          ("carlos@exemplo.com", "carlos123", "Carlos"),
          ("roberto@exemplo.com", "roberto123", "Roberto");

select * from db_semana08.Clientes;

select * from db_semana08.Clientes order by nome asc;

select * from db_semana08.Clientes order by nome desc;

