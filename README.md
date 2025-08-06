# 🔐 Sistema de coleção de cartas 

API RESTful para gerenciamento de usuários e cartas colecionáveis. Possui autenticação JWT, sistema de pacotes aleatórios por raridade e documentação Swagger.

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Flask
- SQLAlchemy
- PyJWT
- Flasgger (Swagger UI)
- MySQL

## ⚙️ Instalação e Execução

Comece criando um ambiente virtual para melhor gerenciamento dos pacotes que serão instalados:

Linux:
```bash
python3 -m venv venv
source venv/bin/activate  
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate    
```

Depois de ter realizado esta etapa de criar o ambiente virtual chegou o momento de instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

Para conseguir rodar a API de fato será necessário um sistema de banco de dados, pode ser de sua preferência, atualize ```/Connection/config.py``` colocando as informações do seu banco de dados lá e também sua senha para o token, exemplo: 

```bash
USER = 'usuario'
PASSWORD = 'senha'
HOST = 'host_do_seu_db'
DB_NAME = 'nome_do_seu_db'

SECRET_KEY = "senha_secreta"
```

Após ter realizado todas estas etapas chegou o momento de rodar o aplicativo flask, inicialmente você irá rodar o comando:

```bash
python3 create_models.py #Linux/MacOS
python create_models.py #Windows
```

Para o funcionamento ocorrer bem, eu disponibilizei um arquivo ```InsertTabelaCarta.sql```
dentro deste arquivo está uma query para popular a tabela de cartas, rode esta query dentro do SGBD de sua preferência.

Finalmente após todas estas etapas está tudo pronto para rodar a API.

```bash
python3 app.py #Linux/MaxOS
python app.py #Windows
```

# ⚠️ Extra

Para ver a documentação feita no Swagger, basta rodar a aplicação e acessar o seguinte link:

```
http://localhost:5000/apidocs
```


# ✅ Consideração final

Este repositório foi criado com um propósito puramente educativo sem qualquer finalidade financeira!

