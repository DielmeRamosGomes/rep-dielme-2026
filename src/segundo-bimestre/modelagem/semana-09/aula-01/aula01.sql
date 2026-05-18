create database if not exists db_livraria;

create table if not exists db_livraria.clientes_online(
    id_cliente int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) not null,
    cidade varchar(100) not null
);

create table if not exists db_livraria.clientes_fisicos(
    id_cliente int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) not null,
    cidade varchar(100) not null
);

insert into db_livraria.clientes_online(nome, email, cidade)
    values('Ana Silva', 'ana@email.com', 'São Paulo'),
          ('Carlos Santos', 'carlos@email.com', 'Rio de Janeiro'),
          ('Bia Oliveira', 'bia@email.com', 'Brasília');

insert into db_livraria.clientes_fisicos(nome, email, cidade)
    values('Carlos Santos', 'carlos@email.com', 'Rio de Janeiro'),
          ('Bia Oliveira', 'bia@email.com', 'Brasília'),
          ('Denis Pereira', 'denis@email.com', 'Salvador');

select * from db_livraria.clientes_online;

select * from db_livraria.clientes_fisicos;

-- 1) UNION: Retorne todos os clientes que compraram em 
-- qualquer uma das lojas (on-line ou física) sem duplicar 
-- informações.

select nome, email, cidade from db_livraria.clientes_online
UNION
select nome, email, cidade from db_livraria.clientes_fisicos;

-- 2) INTERSECT: Encontre os clientes que compraram tanto na 
-- loja on-line quanto na loja física.

select nome, email, cidade from db_livraria.clientes_online
INTERSECT
select nome, email, cidade from db_livraria.clientes_fisicos;

-- 3) EXCEPT: Liste os clientes que compraram na loja on-line,
-- mas não compraram na loja física.

select nome, email, cidade from db_livraria.clientes_online
EXCEPT
select nome, email, cidade from db_livraria.clientes_fisicos;




