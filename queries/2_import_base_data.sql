set sql_mode = "";

load data infile '/var/lib/mysql-files/Escola.csv' into
table censo.escola fields terminated by '|' enclosed by '"' lines terminated by '\r\n' ignore 1 lines;

load data infile '/var/lib/mysql-files/Turma.csv' into
table censo.turma fields terminated by '|' enclosed by '"' lines terminated by '\r\n' ignore 1 lines;

load data infile '/var/lib/mysql-files/Docente.csv' into
table censo.docente fields terminated by '|' enclosed by '"' lines terminated by '\r\n' ignore 1 lines;

load data infile '/var/lib/mysql-files/Matricula.csv' into
table censo.matricula fields terminated by '|' enclosed by '"' lines terminated by '\r\n' ignore 1 lines;
