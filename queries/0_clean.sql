use censo;

drop table if exists bookmark;

drop table if exists usuario;

drop table if exists matricula;

drop table if exists docente;

drop table if exists turma;

drop table if exists escola;

# permissões
revoke all on censo.* from 'grupo3';

grant
select, insert, update, delete
on censo.* to 'grupo3';
