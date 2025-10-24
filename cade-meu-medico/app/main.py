from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from app.api.v1.api import api_router 
from app.core.config import settings 
 
app = FastAPI( 
    title="Cade meu Medico? API", 
    description="API para busca de medicos por especialidade e localizacao.", 
    version="1.0.0", 
    openapi_url="/api/v1/openapi.json", 
    docs_url="/api/docs", 
    redoc_url="/api/redoc" 
) 
 
# Configuracao do CORS 
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
) 
 
# Incluir o roteador principal da v1 
app.include_router(api_router, prefix="/api/v1") 
 
@app.get("/") 
def read_root(): 
    return {"message": "Bem-vindo a API 'Cade meu Medico?'", "docs": "/api/docs"} 
