from fastapi import APIRouter, Depends, Query 
from sqlalchemy.orm import Session 
from typing import List, Optional 
from app.schemas import doctor as doctor_schema 
from app.crud import crud_doctor 
from app.api.v1 import deps 
 
router = APIRouter() 
 
@router.get("/doctors", response_model=List[doctor_schema.Doctor]) 
def search_doctors( 
    *, 
    db: Session = Depends(deps.get_db), 
    name: Optional[str] = Query(None), 
    specialty: Optional[str] = Query(None), 
    city: Optional[str] = Query(None) 
): 
    Busca avancada de medicos. Endpoint aberto. 
    doctors = crud_doctor.search_doctors(db, name=name, specialty=specialty, city=city) 
    return doctors 
