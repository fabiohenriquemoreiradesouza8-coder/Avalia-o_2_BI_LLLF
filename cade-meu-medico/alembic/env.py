import os, sys 
from logging.config import fileConfig 
 
from sqlalchemy import engine_from_config, pool 
from alembic import context 
 
# Importar a base e os modelos 
sys.path.insert(0, os.getcwd()) 
from app.db.base_class import Base 
from app.db import models # Importa todos os seus modelos 
 
# Configurar o objeto target_metadata 
target_metadata = Base.metadata 
 
config = context.config 
 
fileConfig(config.config_file_name) 
 
def run_migrations_offline(): 
    """Run migrations in 'offline' mode. """ 
    url = config.get_main_option("sqlalchemy.url") 
    context.configure( 
        url=url, target_metadata=target_metadata, literal_binds=True 
    ) 
    with context.begin_transaction(): 
        context.run_migrations() 
 
def run_migrations_online(): 
    """Run migrations in 'online' mode. """ 
    connectable = engine_from_config( 
        config.get_section(config.config_ini_section, {}), 
        prefix="sqlalchemy.", 
        poolclass=pool.NullPool, 
    ) 
    with connectable.connect() as connection: 
        context.configure( 
            connection=connection, target_metadata=target_metadata 
        ) 
        try: 
            with context.begin_transaction(): 
                context.run_migrations() 
        except Exception as e: 
            print(f"Erro na migracao: {e}") 
            raise 
 
if context.is_offline_mode(): 
    run_migrations_offline() 
else: 
    run_migrations_online() 
