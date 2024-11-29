use labbd;

alter table escola add primary key (CO_ENTIDADE);

alter table turma add primary key (ID_TURMA);

alter table turma
add foreign key (CO_ENTIDADE) references escola (CO_ENTIDADE);

alter table docente add primary key (CO_PESSOA_FISICA, ID_TURMA);

alter table docente
add foreign key (CO_ENTIDADE) references escola (CO_ENTIDADE);

alter table docente
add foreign key (ID_TURMA) references turma (ID_TURMA);

alter table matricula add primary key (ID_MATRICULA);

alter table matricula
add foreign key (CO_ENTIDADE) references escola (CO_ENTIDADE);

alter table matricula modify CO_PESSOA_FISICA bigint not null;

alter table matricula
add foreign key (ID_TURMA) references turma (ID_TURMA);

drop table if exists usuario;
create table usuario (
    id_usuario int not null auto_increment,
    nome varchar(100) not null,
    email varchar(100) unique not null,
    data_cadastro datetime not null,
    gerencial boolean not null default false,
    primary key (id_usuario)
);

drop table if exists bookmark;
create table bookmark (
    id_bookmark int not null auto_increment,
    id_usuario int not null,
    id_entidade int not null,
    primary key (id_bookmark),
    foreign key (id_usuario) references usuario (id_usuario),
    foreign key (id_entidade) references escola (CO_ENTIDADE)
);

-- Modificar campo data de cadastro da tabela Usuário para aceitar como default a data atual;
alter table usuario
modify data_cadastro datetime default current_timestamp;

alter table usuario add senha varchar(40) not null;

create trigger hash_password before
insert
    on usuario for each row
set
    new.senha = SHA (new.senha);


-- Adicione o campo data de nascimento na tabela Usuario;
alter table usuario add data_nascimento date;

-- insert into
--     usuario (
--         nome,
--         email,
--         senha,
--         data_nascimento
--     )
-- values (
--         'admin',
--         'admin@unesp.br',
--         'admin',
--         '1999-01-01'
--     );

-- insert into bookmark (id_usuario, id_entidade) values (1, 35004193);

-- delete from bookmark where id_usuario = 1 and id_entidade = 35004193;

-- delete from usuario where id_usuario = 1;
