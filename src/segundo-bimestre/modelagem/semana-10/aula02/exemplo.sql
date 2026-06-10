create database if not exists db_escola;

create table if not exists db_escola.tb_alunos(
    id int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) not null unique,
    ra varchar(100) not null
);

create table if not exists db_escola.tb_disciplina(
    id int auto_increment primary key,
    nome varchar(100) not null
); 

create table if not exists db_escola.tb_aluno_disciplina(
    id int auto_increment primary key,
    disciplina_id int not null,
    aluno_id int not null,
    foreign key (disciplina_id) references db_escola.tb_disciplina(id),
    foreign key (aluno_id) references db_escola.tb_alunos(id)
); 

insert into db_escola.tb_alunos(nome, email, ra)
values("Lucas", "lucas@exemplo.com", "1234"),
      ("Gabriel", "gabriel@exemplo.com", "5678");

insert into db_escola.tb_disciplina(nome)
values("Modelagem"), 
      ("PBE");

insert into db_escola.tb_aluno_disciplina(disciplina_id, aluno_id)
values(1, 1),
      (2, 1),
      (1, 2);

select a.nome, d.nome from db_escola.tb_alunos as a
join db_escola.tb_aluno_disciplina as ad
on a.id = ad.aluno_id 
join db_escola.tb_disciplina as d
on d.id = ad.disciplina_id
where a.nome = "Lucas";

