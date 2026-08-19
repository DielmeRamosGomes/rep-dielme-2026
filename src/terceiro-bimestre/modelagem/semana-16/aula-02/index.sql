create database if not exists db_index;

create table if not exists db_index.clientes(
    id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null unique
);

create index idx_nome on db_index.clientes(nome);

create index idx_nome_email on db_index.clientes(nome, email);

insert into db_index.clientes(nome, email)
values("Carlos José", "carlosj@exemplo.com"),
      ("Carlos Henrique", "carlosh@exemplo.com"),
      ("Carlos Daniel", "carlosd@exemplo.com");

select * from db_index.clientes;

EXPLAIN select * from db_index.clientes
where nome = 'Carlos José';

-- lista os indices de uma tabela
show index from db_index.clientes;

-- Ver a definição da tabela com os índices
show create table db_index.clientes;

-- Verificar se o índice está sendo usado
EXPLAIN select * from db_index.clientes
where nome = 'Carlos José';

EXPLAIN select * from db_index.clientes
where nome = "Carlos José" and email = "carlosj@exemplo.com";

