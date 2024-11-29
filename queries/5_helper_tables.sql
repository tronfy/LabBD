-- TP_SITUACAO_FUNCIONAMENTO
drop table if exists cat_situacao;
create table cat_situacao (
  id int primary key,
  descricao varchar(30)
);
insert into cat_situacao (id, descricao) values
(1, 'Em Atividade'),
(2, 'Paralisada'),
(3, 'Extinta (ano do Censo)'),
(4, 'Extinta em Anos Anteriores');

-- TP_LOCALIZACAO
drop table if exists cat_localizacao;
create table cat_localizacao (
  id int primary key,
  descricao varchar(10)
);
insert into cat_localizacao (id, descricao) values
(1, 'Urbana'),
(2, 'Rural');

-- TP_DEPENDENCIA
drop table if exists cat_dependencia;
create table cat_dependencia (
  id int primary key,
  descricao varchar(10)
);
insert into cat_dependencia (id, descricao) values
(1, 'Federal'),
(2, 'Estadual'),
(3, 'Municipal'),
(4, 'Privada');

-- CO_MUNICIPIO
drop table if exists cat_municipio;
create table cat_municipio (
  id int primary key,
  nome varchar(20)
);
insert into cat_municipio (id, nome) values
(3543907, 'Rio Claro');


drop view if exists escola_matriculas;
create view escola_matriculas as
  select e.CO_ENTIDADE, count(m.ID_MATRICULA) as n_matriculas from escola e
  left join matricula m on e.CO_ENTIDADE = m.CO_ENTIDADE group by e.CO_ENTIDADE;

drop view if exists escola_turmas;
create view escola_turmas as
  select e.CO_ENTIDADE, count(t.ID_TURMA) as n_turmas from escola e
  left join turma t on e.CO_ENTIDADE = t.CO_ENTIDADE group by e.CO_ENTIDADE;

drop view if exists escola_docentes;
create view escola_docentes as
  select e.CO_ENTIDADE, count(distinct d.CO_PESSOA_FISICA) as n_docentes from escola e
  left join docente d on d.CO_ENTIDADE = e.CO_ENTIDADE group by e.CO_ENTIDADE;

-- # Nível de ensino por 
-- # EI:  1, 2
-- # EF1: 4, 5, 6, 7, 14, 15, 16, 17, 18
-- # EF2: 8, 9, 10, 11, 19, 20, 21, 41
-- # EM:  25, 26, 27, 28, 29, 35, 36, 37, 38
-- # EJA: 65, 67, 69, 70, 71, 72, 73, 74
-- # EP:  30, 31, 32, 33, 34, 39, 40, 68
drop table if exists cat_nivel_ensino;
create table cat_nivel_ensino (
  id int primary key,
  nivel varchar(10)
);
insert into cat_nivel_ensino (id, nivel) values
(1, 'EI'),
(2, 'EI'),
(4, 'EF1'),
(5, 'EF1'),
(6, 'EF1'),
(7, 'EF1'),
(14, 'EF1'),
(15, 'EF1'),
(16, 'EF1'),
(17, 'EF1'),
(18, 'EF1'),
(8, 'EF2'),
(9, 'EF2'),
(10, 'EF2'),
(11, 'EF2'),
(19, 'EF2'),
(20, 'EF2'),
(21, 'EF2'),
(41, 'EF2'),
(25, 'EM'),
(26, 'EM'),
(27, 'EM'),
(28, 'EM'),
(29, 'EM'),
(35, 'EM'),
(36, 'EM'),
(37, 'EM'),
(38, 'EM'),
(65, 'EJA'),
(67, 'EJA'),
(69, 'EJA'),
(70, 'EJA'),
(71, 'EJA'),
(72, 'EJA'),
(73, 'EJA'),
(74, 'EJA'),
(30, 'EP'),
(31, 'EP'),
(32, 'EP'),
(33, 'EP'),
(34, 'EP'),
(39, 'EP'),
(40, 'EP'),
(68, 'EP');
