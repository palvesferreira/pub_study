FROM mcr.microsoft.com/devcontainers/python:3.11

# Node.js para Svelte
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Instalações úteis
RUN pip install --upgrade pip

# Cria usuário vscode se não existir
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    || true

USER $USERNAME