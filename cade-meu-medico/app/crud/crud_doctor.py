from sqlalchemy.orm import Session, joinedload 
from typing import List, Optional 
from app.db import models 
from app.schemas import doctor as doctor_schema 
from app.crud import crud_auxiliary 
 
    return db.query(models.Doctor).filter(models.Doctor.crm == crm).first() 
 
    return db.query(models.Doctor).options( 
        joinedload(models.Doctor.specialties), 
        joinedload(models.Doctor.cities) 
    ).filter(models.Doctor.id == doctor_id).first() 
 
def get_doctors(db: Session, skip: int = 0, limit: int = 100) -
    return db.query(models.Doctor).options( 
        joinedload(models.Doctor.specialties), 
        joinedload(models.Doctor.cities) 
    ).order_by(models.Doctor.name).offset(skip).limit(limit).all() 
 
def create_doctor(db: Session, doctor: doctor_schema.DoctorCreate) -
    db_doctor = models.Doctor(name=doctor.name, crm=doctor.crm) 
 
    # Associar especialidades 
    for spec_id in doctor.specialty_ids: 
        spec = crud_auxiliary.get_specialty_by_id(db, spec_id) 
        if spec: 
            db_doctor.specialties.append(spec) 
 
    # Associar cidades 
    for city_id in doctor.city_ids: 
        city = crud_auxiliary.get_city_by_id(db, city_id) 
        if city: 
            db_doctor.cities.append(city) 
 
    db.add(db_doctor) 
    db.commit() 
    db.refresh(db_doctor) 
    return db_doctor 
 
def update_doctor(db: Session, db_doctor: models.Doctor, doctor_in: doctor_schema.DoctorUpdate) -
    update_data = doctor_in.model_dump(exclude_unset=True) 
 
    if "specialty_ids" in update_data: 
        db_doctor.specialties.clear() 
        for spec_id in update_data["specialty_ids"]: 
            spec = crud_auxiliary.get_specialty_by_id(db, spec_id) 
            if spec: 
                db_doctor.specialties.append(spec) 
        del update_data["specialty_ids"] 
 
    if "city_ids" in update_data: 
        db_doctor.cities.clear() 
        for city_id in update_data["city_ids"]: 
            city = crud_auxiliary.get_city_by_id(db, city_id) 
            if city: 
                db_doctor.cities.append(city) 
        del update_data["city_ids"] 
 
    for field, value in update_data.items(): 
        setattr(db_doctor, field, value) 
 
    db.add(db_doctor) 
    db.commit() 
    db.refresh(db_doctor) 
    return db_doctor 
 
def delete_doctor(db: Session, doctor_id: int): 
    db_doctor = db.query(models.Doctor).get(doctor_id) 
    if db_doctor: 
        db.delete(db_doctor) 
        db.commit() 
    return db_doctor 
 
def search_doctors(db: Session, name: Optional[str], specialty: Optional[str], city: Optional[str]) -
    query = db.query(models.Doctor).options( 
        joinedload(models.Doctor.specialties), 
        joinedload(models.Doctor.cities) 
    ) 
 
    if name: 
        query = query.filter(models.Doctor.name.ilike(f"%%{name}%%")) 
 
    if specialty: 
        query = query.join(models.Doctor.specialties).filter(models.Specialty.name.ilike(f"%%{specialty}%%")) 
 
    if city: 
        query = query.join(models.Doctor.cities).filter(models.City.name.ilike(f"%%{city}%%")) 
 
    return query.order_by(models.Doctor.name).all() 
