# 📘 LDW Merge Skills API

Sistema full stack para gerenciamento de **Hosts (empresas), Games e Players**, desenvolvido com **Flask + SQLAlchemy + MySQL** no backend e **Flet (Python UI)** no frontend.

---

## 🚀 Tecnologias Utilizadas

### Backend
- Python 3.14
- Flask
- SQLAlchemy (ORM)
- MySQL
- Flasgger (Swagger UI)
- HTTP REST API

### Frontend
- Flet (Python UI Framework)
- HTTPX (consumo da API)

### Ferramentas
- UV (gerenciador de dependências)
- Tailwind CSS (Landing Page)

---

## 📁 Estrutura do Projeto


full-games/
│
├── apps/
│ ├── backend/
│ │ └── src/
│ │ ├── app.py
│ │ ├── database.py
│ │ ├── models/
│ │ └── routes/
│ │
│ └── frontend/
│ ├── main.py
│ ├── src/
│ │ ├── api.py
│ │ ├── views/
│ │ └── components/
│
├── landing/
│ └── index.html
│
└── README.md


---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/ldw-merge-skills.git
cd full-games
2. Backend (Flask API)
cd apps/backend

# instalar dependências
uv sync

# rodar aplicação
uv run flask --app src/app run

📍 API:

http://127.0.0.1:5000

📘 Swagger:

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
GET /hosts/
POST /hosts/
Games
GET /games/
POST /games/
Players
GET /players/
POST /players/
Health
GET /health/
🧠 Arquitetura
API REST com Flask
ORM com SQLAlchemy
Banco MySQL com relacionamento:
Host → Games
Game → Players
Frontend desktop com Flet
Comunicação via HTTPX
📦 Gerenciamento de dependências

Este projeto utiliza uv:

uv sync
🎨 Landing Page

Página estática com Tailwind CSS contendo:

Descrição do sistema
Tecnologias utilizadas
Rotas da API
Instruções de execução
⚠️ Problemas comuns
❌ 308 Redirect

Sempre usar barra final:

/hosts/
/games/
/players/
❌ Foreign Key Error

O host_id precisa existir antes de criar um game.

👨‍💻 Autor

Lucas Parada
