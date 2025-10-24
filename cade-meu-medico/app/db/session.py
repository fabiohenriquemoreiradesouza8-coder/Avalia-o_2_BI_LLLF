from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from app.core.config import settings 
 
engine = create_engine(settings.DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
 
def get_db(): 
    """Dependencia do FastAPI para obter uma sessao do banco de dados.""" 
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close() 
