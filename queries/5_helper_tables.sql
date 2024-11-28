-- TP_SITUACAO_FUNCIONAMENTO
drop table if exists cat_situacao;
create table cat_situacao (
  id int primary key,
  descricao varchar(50)
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
  descricao varchar(50)
);
insert into cat_localizacao (id, descricao) values
(1, 'Urbana'),
(2, 'Rural');

-- TP_DEPENDENCIA
drop table if exists cat_dependencia;
create table cat_dependencia (
  id int primary key,
  descricao varchar(50)
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
  nome varchar(50)
);
insert into cat_municipio (id, nome) values
(3543907, 'Rio Claro');


drop view if exists escola_matriculas;
create view escola_matriculas as
  select e.CO_ENTIDADE, count(m.ID_MATRICULA) as n_matriculas from escola e
  left join matricula m on e.CO_ENTIDADE = m.CO_ENTIDADE group by m.CO_ENTIDADE;

drop view if exists escola_turmas;
create view escola_turmas as
  select e.CO_ENTIDADE, count(t.ID_TURMA) as n_turmas from escola e
  left join turma t on e.CO_ENTIDADE = t.CO_ENTIDADE group by e.CO_ENTIDADE;

drop view if exists escola_docentes;
create view escola_docentes as
  select e.CO_ENTIDADE, count(distinct d.CO_PESSOA_FISICA) as n_docentes from escola e
  left join docente d on d.CO_ENTIDADE = e.CO_ENTIDADE group by e.CO_ENTIDADE;

