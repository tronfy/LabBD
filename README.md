# LabBD

1. Se no Windows, abrir o Docker Desktop para iniciar o docker daemon.

2. Iniciar o container. O MySQL leva alguns segundos para inicializar.
```
docker compose up --build -d
```

3. Conectar pelo Workbench ou [cweijan.vscode-mysql-client2](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-mysql-client2).

| campo | valor |
| --- | --- |
| host | localhost |
| porta | 33061 |
| db/schema | censo |
| user | root |
| senha | c6h5bwInqtKJKmiuPcBQ0A |

4. Remover todas as tabelas e rodar todas as queries: `./run_all.bat`
