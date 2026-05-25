create database if not exists db_logistica;

create table if not exists db_logistica.veiculos(
    id_veiculo int auto_increment primary key,
    modelo varchar(100) not null,
    ano int not null,
    capacidade decimal(10, 2) not null
);

create table if not exists db_logistica.entregas(
    id_entrega int auto_increment primary key,
    id_veiculo int not null,
    data_entrega date not null,
    cidade varchar(100) not null,
    peso_entrega decimal(10, 2) not null,
    foreign key(id_veiculo) references db_logistica.veiculos(id_veiculo)
);

insert into db_logistica.veiculos(modelo, ano, capacidade)
values  ('Caminhão A', 2018, 10.00),
        ('Caminhão B', 2020, 15.00),
        ('Caminhão X', 2015, 3.00),
        ('Caminhão C', 2022, 12.00);

insert into db_logistica.entregas(id_veiculo, data_entrega, cidade, peso_entrega)
values  (1, '2024-08-01', 'São Paulo', 8.0),
        (2, '2024-08-03', 'Rio de Janeiro', 12.0),
        (3, '2024-08-05', 'Brasília', 2.5),
        (1, '2024-08-07', 'Belo Horizonte', 9.5),
        (4, '2024-08-10', 'Salvador', 11.0),
        (2, '2024-08-12', 'São Paulo', 13.5),
        (3, '2024-08-14', 'Brasília', 2.0);

select * from db_logistica.veiculos;

select * from db_logistica.entregas;

-- 1. Filtrar entregas feitas em São Paulo e após 2024-08-01 (usando WHERE)
select * from db_logistica.entregas
    where cidade = 'São Paulo' and data_entrega > '2024-08-01';

-- 2. Filtrar veículos com capacidade de carga maior que 10 toneladas (usando WHERE)
select * from db_logistica.veiculos
    where capacidade > 10.00;

-- 3. Agrupar entregas por cidade com peso total de entregas acima de 15 toneladas (usando HAVING)
select cidade, sum(peso_entrega) as total_peso
    from db_logistica.entregas
        group by cidade
            having total_peso > 15.00;

-- HAVING é usado para filtrar grupos de dados após a agregação.

-- 4. Identificar veículos com entregas acima de 10 toneladas no total (usando HAVING)
SELECT v.modelo, SUM(e.peso_entrega) AS total_peso_entregas
    FROM db_logistica.veiculos as v
        JOIN db_logistica.entregas as e ON v.id_veiculo = e.id_veiculo
            GROUP BY v.modelo
                HAVING total_peso_entregas > 10.0;

