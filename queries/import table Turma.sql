SET sql_mode = "";
load data infile 'C:\\Users\\Bruno\\Desktop\\Unesp\\LabBD\\2024\\Trabalho\\selecionados\\Turmas Rio Claro 2017.csv'
into table labbd.turma
fields terminated by '|'
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
;