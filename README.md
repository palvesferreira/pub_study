# Como iniciar o ambiente de desenvolvimento (Dev Container)

Siga os passos abaixo para iniciar o ambiente de desenvolvimento usando o Dev Container no VS Code:

## Pré-requisitos

- [Docker](https://www.docker.com/get-started) instalado e em execução.
- [Visual Studio Code](https://code.visualstudio.com/) instalado.
- Extensão [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) instalada no VS Code.

## Passos para iniciar

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd finance-control
   ```

2. **Abra o projeto no VS Code:**

   ```bash
   code .
   ```

3. **Abra o ambiente Dev Container:**

   - No VS Code, pressione `F1` e digite:  
     `Dev Containers: Reopen in Container`
   - Aguarde o VS Code construir e iniciar o container.

4. **Inicie os servidores:**

   - No terminal do container, execute:

     ```bash
     # Inicie o backend FastAPI
     uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
     ```

     ```bash
     # Em outro terminal, inicie o frontend Svelte
     cd frontend
     npm run dev -- --host
     ```

5. **Acesse as aplicações:**
   - Backend (FastAPI): http://localhost:8000
   - Frontend (Svelte): http://localhost:5173

---

Pronto! O ambiente está configurado para desenvolvimento integrado com FastAPI e Svelte.# pub_study
