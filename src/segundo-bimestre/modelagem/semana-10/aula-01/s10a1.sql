create database if not exists db_s10a1;

create table if not exists db_s10a1.produtos(
    id_produto int auto_increment primary key,
    nome varchar(100) not null,
    preco decimal(10, 2) not null
);

create table if not exists db_s10a1.clientes(
    id_cliente int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100)  unique not null
);

create table if not exists db_s10a1.vendas(
    id_venda int auto_increment primary key,
    id_produto int not null,
    data_venda date not null,
    quantidade int not null,
    id_cliente int not null,
    foreign key (id_cliente) references db_s10a1.clientes(id_cliente),
    foreign key (id_produto) references db_s10a1.produtos(id_produto)
);

create table if not exists db_s10a1.vendas_clientes(
    id_venda int not null,
    id_cliente int not null,
    primary key (id_venda, id_cliente), 
    foreign key (id_venda) references db_s10a1.vendas(id_venda),
    foreign key (id_cliente) references db_s10a1.clientes(id_cliente)
);

insert into db_s10a1.produtos (nome, preco) values
('Televisão', 1500.00),
('Geladeira', 2000.00),
('Micro-ondas', 500.00);

select * from db_s10a1.produtos;

insert into db_s10a1.clientes (nome, email) values
('João Silva', 'joao@exemplo.com'),
('Maria Oliveira', 'maria@exemplo.com'),
('Carlos Santos', 'carlos@exemplo.com');

select * from db_s10a1.clientes;

insert into db_s10a1.vendas (id_produto, data_venda, quantidade, id_cliente) values
(1, '2024-01-15', 2, 1),
(2, '2024-02-20', 1, 2),
(3, '2023-03-10', 3, 3),
(1, '2023-04-05', 1, 1),
(2, '2024-05-12', 2, 2);

select * from db_s10a1.vendas;

-- 2. Imagine que você deseja preencher a tabela 
-- Vendas_Clientes com os registros de vendas realizadas no ano 
-- de 2024, associando-as aos clientes. Crie uma subconsulta para 
-- inserir esses dados:

insert into db_s10a1.vendas_clientes (id_venda, id_cliente)
select v.id_venda, c.id_cliente
    from db_s10a1.vendas v
    join db_s10a1.clientes c on v.id_cliente = c.id_cliente
    where year(v.data_venda) = 2024;

select * from db_s10a1.vendas_clientes;

create table if not exists db_s10a1.fornecedores(
    id_fornecedor int auto_increment primary key,
    nome_fornecedor varchar(100) not null,
    cidade varchar(100) not null
);

create table if not exists db_s10a1.categoria(
    id_categoria int auto_increment primary key,
    nome_categoria varchar(100) not null
);

create table if not exists db_s10a1.produtos_categoria(
    id_produto int not null,
    id_categoria int not null,
    primary key (id_produto, id_categoria),
    foreign key (id_produto) references db_s10a1.produtos(id_produto),
    foreign key (id_categoria) references db_s10a1.categoria(id_categoria)
);

create table if not exists db_s10a1.fornecedores_produtos(
    id_fornecedor int not null,
    id_produto int not null,
    primary key (id_produto, id_fornecedor),
    foreign key (id_produto) references db_s10a1.produtos(id_produto),
    foreign key (id_fornecedor) references db_s10a1.fornecedores(id_fornecedor)
);

insert into db_s10a1.categoria(nome_categoria) values
('Eletrodomésticos'),
('Eletroportáteis');

insert into db_s10a1.fornecedores(nome_fornecedor, cidade) values
('Fornecedor A', 'São Paulo'),
('Fornecedor B', 'Rio de Janeiro');

insert into db_s10a1.fornecedores_produtos (id_fornecedor, id_produto) values
(1, 1), -- Fornecedor A fornece Televisão
(1, 2), -- Fornecedor A fornece Geladeira
(2, 3); -- Fornecedor B fornece Micro-ondas

select * from db_s10a1.fornecedores_produtos;

-- Suponha que os produtos "Televisão" e "Geladeira" devem ser 
-- categorizados como "Eletrodomésticos", e "Micro-ondas", como 
-- "Eletroportáteis". Insira esses dados na tabela 
-- Produtos_Categorias, usando uma subconsulta para buscar os IDs 
-- dos produtos e das categorias.

insert into db_s10a1.produtos_categoria (id_produto, id_categoria)
select p.id_produto, c.id_categoria
    from db_s10a1.produtos p
    join db_s10a1.categoria c on 
        (p.nome = 'Televisão' and c.nome_categoria = 'Eletrodomésticos') or
        (p.nome = 'Geladeira' and c.nome_categoria = 'Eletrodomésticos') or
        (p.nome = 'Micro-ondas' and c.nome_categoria = 'Eletroportáteis');

select * from db_s10a1.produtos_categoria;
