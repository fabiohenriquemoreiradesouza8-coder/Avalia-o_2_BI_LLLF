# Avaliacao_2_BI_LLLF
Vamos optar por uma stack moderna, eficiente e alinhada com as melhores práticas do mercado para Python.

Linguagem: Python 3.10+

Framework Web: FastAPI. É a escolha ideal para este projeto por ser moderno, extremamente rápido (comparável a NodeJS e Go), fácil de usar e, o mais importante, gera documentação OpenAPI (Swagger UI) automaticamente, o que já cumpre um dos requisitos obrigatórios com quase nenhum esforço extra.

Banco de Dados: PostgreSQL. É um banco de dados relacional poderoso, open-source e muito bem suportado pela comunidade Python.

ORM (Object-Relational Mapper): SQLAlchemy 2.0. É o ORM mais popular e completo para Python. Ele permite que você interaja com o banco de dados usando objetos Python, o que torna o código mais seguro, legível e fácil de manter.

Validação de Dados: Pydantic V2. O FastAPI é construído sobre o Pydantic, que permite declarar a "forma" dos seus dados (schemas) de maneira simples e intuitiva, garantindo validações robustas tanto na entrada quanto na saída da API.

Autenticação JWT: python-jose. Uma biblioteca sólida para codificar, decodificar e validar tokens JWT.

Hashing de Senhas: Passlib com Bcrypt. Essencial para armazenar as senhas dos usuários de forma segura.

Containerização: Docker e Docker Compose, conforme solicitado.

Versionamento: Git (com o repositório hospedado no GitHub
