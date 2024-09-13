SET sql_mode = "";

load data infile '/var/lib/mysql-files/Escola.csv' into
table censo.escola fields terminated by '|' enclosed by '"' lines terminated by '\r\n' ignore 1 lines;
