# CotacaoB3

## Descrição do Projeto

O **CotacaoB3** é uma aplicação desenvolvida em **Django** para consultar e gerenciar cotações de ativos financeiros da **B3** (Bolsa de Valores do Brasil). A aplicação inclui funcionalidades para cadastro de ativos, monitoramento de cotações, e envio de alertas com base em limites configurados.

## Requisitos

Certifique-se de ter os seguintes itens instalados no seu sistema:

- **Python 3.8** ou superior
- **Docker** e **Docker Compose** (opcional, para executar a aplicação com containers)
- **Redis** (necessário para tarefas assíncronas com Celery)
- **pip** (gerenciador de pacotes do Python)
- Banco de dados **SQLite** (ou outro configurado no Django)

## Instalação

### Sem Docker

1. Clone o repositório:

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd CotacaoB3
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure o Redis:
    Certifique-se de que o Redis está instalado e em execução. O Celery utiliza o Redis como backend.

5. Realize as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

### Com Docker

1. Certifique-se de que Docker e Docker Compose estão instalados no seu sistema.

2. Execute os containers:

    ```bash
    docker-compose up --build
    ```

## Execução

### Sem Docker

1. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

2. Inicie o Celery para executar tarefas assíncronas:

    ```bash
    celery -A CotacaoB3 worker --loglevel=info
    ```

3. Acesse a aplicação no navegador pelo endereço:

    ```
    http://127.0.0.1:8000
    ```

### Com Docker

A aplicação e todos os serviços (Redis, Django, Celery) serão iniciados automaticamente pelos containers. Acesse pelo navegador em:

    ```
    http://127.0.0.1:8000
    ```

## Estrutura do Projeto

- **CotacaoB3/**: Diretório principal do projeto.
  - **settings.py**: Configurações do Django.
  - **urls.py**: Roteamento de URLs.
  - **wsgi.py**: Configuração para serviços WSGI.
  - **celery.py**: Configurações do Celery para tarefas assíncronas.
  
- **ativos/**: App principal da aplicação.
  - **models.py**: Modelos de dados para os ativos.
  - **forms.py**: Formulários para entrada de dados.
  - **views.py**: Lógica das views.
  - **tasks.py**: Tarefas assíncronas com Celery.

- **templates/**: Arquivos HTML.
- **static/**: Arquivos estáticos (CSS e JS).
- **requirements.txt**: Lista de dependências do projeto.
- **docker-compose.yml**: Arquivo para configuração de containers Docker.
- **Dockerfile**: Configuração do ambiente Docker.

## Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Fork o repositório.
2. Crie uma branch para sua feature/bugfix:

    ```bash
    git checkout -b minha-feature
    ```

3. Envie suas alterações:

    ```bash
    git commit -m "Minha contribuição"
    git push origin minha-feature
    ```

4. Abra um Pull Request.

## Autor

[Lucas Lima]

## Licença

Este projeto está licenciado sob a **MIT License**.
