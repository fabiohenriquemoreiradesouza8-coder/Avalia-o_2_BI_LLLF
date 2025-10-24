from sqlalchemy.orm import Session 
from app.db import models 
 
def get_specialties(db: Session): 
    return db.query(models.Specialty).order_by(models.Specialty.name).all() 
 
def get_cities(db: Session): 
    return db.query(models.City).order_by(models.City.name).all() 
 
def get_specialty_by_id(db: Session, specialty_id: int): 
    return db.query(models.Specialty).filter(models.Specialty.id == specialty_id).first() 
 
def get_city_by_id(db: Session, city_id: int): 
    return db.query(models.City).filter(models.City.id == city_id).first() 
