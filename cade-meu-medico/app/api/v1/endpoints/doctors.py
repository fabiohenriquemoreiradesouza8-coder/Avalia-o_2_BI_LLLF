from fastapi import APIRouter, Depends, HTTPException, status, Query 
from sqlalchemy.orm import Session 
from typing import List 
from app.schemas import doctor as doctor_schema 
from app.schemas import msg as msg_schema 
from app.crud import crud_doctor 
from app.api.v1 import deps 
from app.db import models 
 
router = APIRouter() 
 
@router.get("", response_model=List[doctor_schema.Doctor]) 
def list_doctors( 
    db: Session = Depends(deps.get_db), 
    skip: int = Query(0, ge=0), 
    limit: int = Query(100, ge=1, le=200) 
): 
    Lista todos os medicos (paginado). Endpoint aberto. 
    doctors = crud_doctor.get_doctors(db, skip=skip, limit=limit) 
    return doctors 
 
@router.get("/{id}", response_model=doctor_schema.Doctor) 
def get_doctor_details( 
    *, 
    db: Session = Depends(deps.get_db), 
    id: int 
): 
    Detalhes de um medico. Endpoint aberto. 
    doctor = crud_doctor.get_doctor(db, doctor_id=id) 
    if not doctor: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medico nao encontrado") 
    return doctor 
 
@router.post("", response_model=doctor_schema.Doctor, status_code=status.HTTP_201_CREATED) 
def create_doctor( 
    *, 
    db: Session = Depends(deps.get_db), 
    doctor_in: doctor_schema.DoctorCreate, 
    current_user: models.User = Depends(deps.get_current_admin_user) 
): 
    Cadastra um novo medico. (Restrito a Admin) 
    doctor = crud_doctor.get_doctor_by_crm(db, crm=doctor_in.crm) 
    if doctor: 
        raise HTTPException( 
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Um medico com este CRM ja esta cadastrado.", 
        ) 
    doctor = crud_doctor.create_doctor(db=db, doctor=doctor_in) 
    return doctor 
 
@router.put("/{id}", response_model=doctor_schema.Doctor) 
def update_doctor( 
    *, 
    db: Session = Depends(deps.get_db), 
    id: int, 
    doctor_in: doctor_schema.DoctorUpdate, 
    current_user: models.User = Depends(deps.get_current_admin_user) 
): 
    Atualiza um medico. (Restrito a Admin) 
    db_doctor = crud_doctor.get_doctor(db, doctor_id=id) 
    if not db_doctor: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medico nao encontrado") 
 
    if doctor_in.crm: 
        existing_doctor = crud_doctor.get_doctor_by_crm(db, crm=doctor_in.crm) 
        if existing_doctor and existing_doctor.id != id: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CRM ja em uso.") 
 
    doctor = crud_doctor.update_doctor(db=db, db_doctor=db_doctor, doctor_in=doctor_in) 
    return doctor 
 
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) 
def delete_doctor( 
    *, 
    db: Session = Depends(deps.get_db), 
    id: int, 
    current_user: models.User = Depends(deps.get_current_admin_user) 
): 
    Remove um medico. (Restrito a Admin) 
    db_doctor = crud_doctor.get_doctor(db, doctor_id=id) 
    if not db_doctor: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medico nao encontrado") 
 
    crud_doctor.delete_doctor(db=db, doctor_id=id) 
    return None 
