-- use labbd;

-- -- Selecione todas as escolas da cidade de Rio Claro;
-- select * from escola;

-- -- Selecione todas as escolas (código e nome) da cidade de Rio Claro;
-- select `CO_ENTIDADE`, `NO_ENTIDADE` from escola;

-- -- Selecione todas as turmas da escola 35021817;
-- select * from turma where `CO_ENTIDADE` = 35021817;

-- -- Selecione todas as matrículas cujos alunos apresentem autismo ou deficiência intelectual;
-- select * from matricula where `IN_AUTISMO` or `IN_DEF_INTELECTUAL`;

-- -- Selecione todos os docentes da escola 35021817 com idade até 45 anos (NU_IDADE);
-- select *
-- from docente
-- where
--     `CO_ENTIDADE` = CO_ENTIDADE
--     and `NU_IDADE` <= 45;

-- -- Selecione todas as escolas que não estejam em funcionamento (TP_SITUACAO_FUNCIONAMENTO);
-- select * from escola where `TP_SITUACAO_FUNCIONAMENTO` != 1;

-- -- Selecione os valores distintos de etapas de ensino (TP_ETAPA_ENSINO) nas Turmas;
-- select distinct (TP_ETAPA_ENSINO) from turma;

-- -- Selecione todas as escola que contenham ‘JOSE’ no nome;
-- select * from escola where `NO_ENTIDADE` like '%JOSE%';

-- -- Selecione as turmas do ensino técnico (TP_ETAPA_ENSINO = 39,40,64) e com nome da escola (use IN);
-- select escola.`NO_ENTIDADE`, turma.`ID_TURMA`
-- from turma
--     join escola on escola.`CO_ENTIDADE` = turma.`CO_ENTIDADE`
-- where
--     turma.`TP_ETAPA_ENSINO` in (39, 40, 64);

-- -- Selecione a quantidade total de computadores de alunos e administrativos na cidade;
-- select sum(`NU_COMP_ADMINISTRATIVO`) + sum(`NU_COMP_ALUNO`) as total_computadores
-- FROM escola;

-- -- Selecione toda as turmas da escola 35021817 e traga: nome da escola, id_turma, os nomes da localização, os nomes da dependência admin (use CASE WHEN e JOIN)
-- select escola.`NO_ENTIDADE`, turma.`ID_TURMA`
--     -- usar CASE WHEN para localização e dep
-- from turma
-- where
--     `CO_ENTIDADE` = 35021817
--     join escola on escola.`CO_ENTIDADE` = turma.`CO_ENTIDADE`;

-- -- Selecione todas as escolas (nome, código) com as respectivas contagens de turmas;

-- -- Selecione todas as escolas (nome, código) com as respectivas contagens de docentes;

-- -- Selecione todas as escolas (nome, código) com as respectivas contagens de matrículas;

-- -- Ordenar o resultados das escolas pela ordem decrescente da contagem de matrículas;

-- -- Ranquear as escolas sobre essa contagem, contando os empates (RANK());

-- -- Selecionar a quantidade de matrículas em escolas de zona rural da cidade de Rio Claro;

-- -- Selecione as escolas que não têm matrículas cadastradas;

-- -- Selecione todas as escolas (nome, código) que tenham turmas do Ensino Médio (TP_ETAPA_ENSINO in (25..27));

-- -- Selecionar as escolas com as contagens de matrículas por nível de ensino, com o campo retornando o nome do nível de ensino;

-- -- Selecione as escolas (nome, código), ordenadas ascendentemente por nome, entre as posições 11 e 20 (use LIMIT e OFFSET)