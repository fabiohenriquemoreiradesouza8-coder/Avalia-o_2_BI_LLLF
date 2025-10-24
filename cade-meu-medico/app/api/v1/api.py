from fastapi import APIRouter 
from app.api.v1.endpoints import auth, users, doctors, search, auxiliary 
 
api_router = APIRouter() 
 
# Incluir todos os roteadores dos endpoints 
api_router.include_router(auth.router, prefix="/auth", tags=["Autenticacao"]) 
api_router.include_router(users.router, prefix="/users", tags=["Usuarios"]) 
api_router.include_router(doctors.router, prefix="/doctors", tags=["Medicos"]) 
api_router.include_router(search.router, prefix="/search", tags=["Busca"]) 
 
# Endpoints auxiliares 
api_router.include_router(auxiliary.router, tags=["Dados Auxiliares"]) 
