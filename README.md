## Como rodar o projeto?

* Abra o terminal.
* Crie um diretório para o projeto e entre nele.
* Clone esse repositório e entre no diretório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
* Rode as fixtures (!Na sequência e apenas uma vez cada uma pra não haver dados replicados!)
* Crie os super usuários (admins) e informe as credênciais
* Inicie o servidor e abra, no navegador, o link http://127.0.0.1:8000/

```
Windowns+R, digite "cmd" e dê Enter

mkdir educacao_transito
cd educacao_transito

git clone https://github.com/naelallves/proj_sinal_transito.git
cd proj_sinal_transito

python -m venv .venv

source .venv/Scripts/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py loaddata placas_fixture.json
python manage.py loaddata categorias_fixture.json
python manage.py loaddata questoes_fixture.json
python manage.py loaddata alternativas_fixture.json
python manage.py loaddata rel_perg_alter_fixture.json

python manage.py createsuperuser OU winpty python manage.py createsuperuser

python manage.py runserver
```