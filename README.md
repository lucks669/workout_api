🏋️ Workout API

API para gerenciamento de atletas, categorias e centros de treinamento, desenvolvida como parte do bootcamp da DIO.

🚀 Tecnologias

Python 3.10+

FastAPI

Uvicorn

SQLAlchemy

Alembic

[SQLite] ou [PostgreSQL] (dependendo da configuração)



---

📦 Como rodar o projeto

1. Clone o repositório

git clone https://github.com/lucks669/workout_api.git
cd workout_api

2. Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instale as dependências

pip install -r requirements.txt

4. Execute as migrações do banco

alembic upgrade head

5. Rode a aplicação

uvicorn workout_api.main:app --reload

A API estará disponível em: 👉 http://127.0.0.1:8000/docs


---

👨‍💻 Autor

Desenvolvido por [Lucas] para o bootcamp da DIO.


---

👉 Agora é só você colar isso no arquivo README.md lá no GitHub e dar commit.

Quer que eu te mostre exatamente onde clicar no GitHub para editar esse README (com setinha tipo tutorial passo a passo)?

