
# Projeto DevOps Azure Challenge

Este é um desafio para testar seus conhecimentos de DevOps na Azure, com foco na configuração de infraestrutura, automação de tarefas e monitoramento de recursos.

## Descrição do Projeto

Este projeto consiste em configurar um servidor na Azure, implementar um script de monitoramento, configurar uma pipeline de CI/CD e criar uma imagem Docker com as configurações do servidor.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Frameworks**: Ansible, Terraform
- **CI/CD**: GitHub Actions
- **Infraestrutura**: Azure

## Como Instalar e Usar o Projeto

### 1. Configurar Infraestrutura com Terraform
1. Navegue até o diretório `terraform`:
   ```bash
   cd terraform
   ```
2. Inicialize e aplique a configuração:
   ```bash
   terraform init
   terraform apply
   cd ..
   ```

### 2. Configurar o Servidor com Ansible
1. Atualize o inventário com o IP do servidor provisionado:
   ```ini
   [todos]
   <IP_DO_SERVIDOR>
   ```
2. Execute o playbook:
   ```bash
   ansible-playbook -i inventario ansible/playbook.yml
   ```

### 3. Rodar o Script de Monitoramento
1. Execute o script Python:
   ```bash
   python3 scripts/monitoramento.py
   ```

### 4. Configurar CI/CD com GitHub Actions
1. Configure os segredos no GitHub (AZURE_WEBAPP_PUBLISH_PROFILE).
2. Faça o commit e o push das alterações no repositório GitHub.

### 5. Construir e Rodar a Imagem Docker
1. Construa a imagem Docker:
   ```bash
   docker build -t monitor-app .
   ```
2. Rode o container:
   ```bash
   docker run -it monitor-app
   ```

### 6. Executar Testes Unitários
1. Execute os testes unitários:
   ```bash
   python3 -m unittest discover -s testes
   ```

## Pipeline CI/CD

### Desenho da Pipeline de CI/CD

```plaintext
+------------------------------------------+
|               Repositório                |
|                  GitHub                  |
+------------------------------------------+
                 |     ^     |
                 |     |     |
                 v     |     v
+------------------------------------------+
|               Evento de Push             |
|            (main branch)                 |
+------------------------------------------+
                 |     ^
                 |     |
                 v     |
+------------------------------------------+
|               Job: Build                 |
| - Configura ambiente Python              |
| - Instala dependências                   |
| - Executa testes unitários               |
+------------------------------------------+
                 |     ^
                 |     |
                 v     |
+------------------------------------------+
|               Job: Docker Build          |
| - Constrói imagem Docker                 |
| - Publica imagem no registro             |
+------------------------------------------+
                 |     ^
                 |     |
                 v     |
+------------------------------------------+
|               Job: Deploy                |
| - Faz o deploy da aplicação              |
| - Usa Azure WebApps Deploy               |
+------------------------------------------+
```

### Definição da Pipeline

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Check out the repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install psutil

    - name: Run unit tests
      run: |
        python -m unittest discover -s testes

  docker_build:
    needs: build
    runs-on: ubuntu-latest

    steps:
    - name: Check out the repository
      uses: actions/checkout@v2

    - name: Build Docker image
      run: |
        docker build -t monitor-app .

    - name: Push Docker image to registry
      run: |
        docker tag monitor-app <seu_registro_docker>/monitor-app:latest
        docker push <seu_registro_docker>/monitor-app:latest

  deploy:
    needs: docker_build
    runs-on: ubuntu-latest

    steps:
    - name: Deploy to Azure
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'monitor-app'
        slot-name: 'production'
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
        package: .
```

## .gitignore

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.env

# Terraform
.terraform/
*.tfstate
*.tfstate.*
terraform.tfvars

# Ansible
*.retry

# Docker
*.dockerignore
Dockerfile
```

## Referência

> This is a challenge by [Coodesh](https://coodesh.com/)

## Finalização e Instruções para a Apresentação

1. Adicione o link do repositório com a sua solução no teste.
2. Adicione o link da apresentação do seu projeto no README.md.
3. Verifique se o README.md está bom e faça o commit final em seu repositório.
4. Envie e aguarde as instruções para seguir. Sucesso e boa sorte. =)
