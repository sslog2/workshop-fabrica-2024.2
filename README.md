# workshop-fabrica-2024.2
Projeto de django de Márcio Souto Maior Sousa

## Sobre o Projeto
- Api de D&D
- Utilizando funções de adicionar_Personagem e adicionar_Jogador
- Excluir Personagem e Jogador

## Relação entidade
- Jogador {1,n} ------> Personagem
- Personagem {n,1} --------> Jogador

## Tecnologias Utilizadas
* [Python](https://www.python.org)
* [Django]([https://www.django](https://www.djangoproject.com/))
* [Git](https://git-scm.com)

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/sslog2/workshop-fabrica-2024.2
    cd workshop-fabrica-2024.2
    ```
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Uso
- Acesse o servidor de desenvolvimento em `http://127.0.0.1:8000/`.

## Estrutura do Projeto

- `manage.py`: Utilitário de linha de comando do Django.
- `project/`: Diretório do projeto Django.
- `app/`: Diretório do aplicativo Django.
