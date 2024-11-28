# LabBD

na cloud vm:
1. iniciar container: `docker compose up -d`, esperar uns segundos

2. remover todas as tabelas e rodar todas as queries: `./run_all.sh`

no local:

1. criear venv: `python -m venv venv`

2. ativar venv: `source ./venv/bin/activate`

3. instalar deps: `pip install -r requirements.txt`

4. rodar streamlit: `python -m streamlit run src/app.py`
