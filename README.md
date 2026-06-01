📘 LDW Merge Skills API

Sistema full stack para gerenciamento de Hosts (empresas), Games e Players, desenvolvido com Flask + SQLAlchemy + MySQL no backend e Flet (Python UI) no frontend.

🚀 Tecnologias Utilizadas
Backend
Python 3.14
Flask
SQLAlchemy (ORM)
MySQL
Flasgger (Swagger UI)
HTTP REST API
Frontend
Flet (UI em Python)
HTTPX (consumo da API)
Ferramentas
UV (gerenciador de dependências)
Tailwind CSS (Landing Page)
📁 Estrutura do Projeto
full-games/
│
├── apps/
│   ├── backend/
│   │   └── src/
│   │       ├── app.py
│   │       ├── database.py
│   │       ├── models/
│   │       └── routes/
│   │
│   └── frontend/
│       ├── main.py
│       ├── src/
│       │   ├── api.py
│       │   ├── views/
│       │   └── components/
│
├── landing/
│   └── index.html
│
└── README.md
⚙️ Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/seu-usuario/ldw-merge-skills.git
cd full-games
2. Backend (Flask API)
cd apps/backend

# instalar dependências
uv sync

# rodar aplicação
uv run flask --app src/app run

API disponível em:

http://127.0.0.1:5000

Swagger:

http://127.0.0.1:5000/apidocs/
3. Frontend (Flet)
cd apps/frontend

uv run python main.py
📌 Funcionalidades
🏢 Hosts
Criar host
Listar hosts
🎮 Games
Criar games vinculados a hosts
Listar games
🧑 Players
Criar players vinculados a games
Listar players
🔗 Rotas da API
Hosts
GET /hosts/ → Lista hosts
POST /hosts/ → Cria host
Games
GET /games/ → Lista games
POST /games/ → Cria game
Players
GET /players/ → Lista players
POST /players/ → Cria player
Health
GET /health/ → Status da API
🧠 Observações Técnicas
Banco relacional com foreign keys
Relacionamentos:
Host → Games
Game → Players
Uso de SQLAlchemy ORM
Validações básicas em POST
Estrutura modular com Blueprints
📦 Gerenciador de Dependências

Este projeto utiliza uv no lugar de pip:

uv sync
🎨 Landing Page

Interface estática em HTML + Tailwind:

Nome do projeto
Descrição
Tecnologias
Rotas da API
Instruções de execução
⚠️ Problemas comuns
❌ 308 Redirect

Use sempre:

/hosts/
/games/
/players/
❌ Foreign Key Error

O host_id precisa existir antes de criar um game.
