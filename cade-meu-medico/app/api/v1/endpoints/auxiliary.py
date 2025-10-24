from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session 
from typing import List 
from app.schemas import auxiliary as aux_schema 
from app.schemas import msg as msg_schema 
from app.crud import crud_auxiliary 
from app.api.v1 import deps 
 
router = APIRouter() 
 
@router.get("/specialties", response_model=List[aux_schema.Specialty]) 
def list_specialties(db: Session = Depends(deps.get_db)): 
    Lista todas as especialidades disponiveis. 
    return crud_auxiliary.get_specialties(db) 
 
@router.get("/cities", response_model=List[aux_schema.City]) 
def list_cities(db: Session = Depends(deps.get_db)): 
    Lista todas as cidades cadastradas. 
    return crud_auxiliary.get_cities(db) 
 
@router.get("/health", response_model=msg_schema.Msg) 
def health_check(): 
    Verifica a saude da aplicacao. 
    return {"message": "Aplicacao esta no ar!"} 
