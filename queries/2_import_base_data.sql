set sql_mode = "";

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Escola.csv' into
table labbd.escola fields terminated by '|' enclosed by '"' lines terminated by '\n' ignore 1 lines;

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Turma.csv' into
table labbd.turma fields terminated by '|' enclosed by '"' lines terminated by '\n' ignore 1 lines;

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Docente.csv' into
table labbd.docente fields terminated by '|' enclosed by '"' lines terminated by '\n' ignore 1 lines;

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Matricula.csv' into
table labbd.matricula fields terminated by '|' enclosed by '"' lines terminated by '\n' ignore 1 lines;