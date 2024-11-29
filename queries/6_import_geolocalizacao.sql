use labbd;

set sql_mode = "";

drop table if exists geolocalizacao;
create table geolocalizacao (
  CO_ENTIDADE int not null auto_increment,
  NO_ENTIDADE varchar(100) not null,
  LAT double not null,
  LON double not null,
  primary key (CO_ENTIDADE)
);

load data infile '/var/lib/mysql-files/Geolocalizacao.csv' into
table geolocalizacao fields terminated by ';' enclosed by '"' lines terminated by '\n' ignore 1 lines;
