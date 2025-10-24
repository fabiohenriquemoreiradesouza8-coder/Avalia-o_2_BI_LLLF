from sqlalchemy.orm import Session 
from app.db import models 
from app.db.session import SessionLocal 
from app.crud import crud_user 
from app.schemas import user as user_schema 
 
# Dados Iniciais de Seed 
CITIES = [ 
    {"name": "Sao Paulo", "state": "SP"}, 
    {"name": "Rio de Janeiro", "state": "RJ"}, 
    {"name": "Curitiba", "state": "PR"}, 
    {"name": "Belo Horizonte", "state": "MG"}, 
    {"name": "Porto Alegre", "state": "RS"}, 
] 
 
SPECIALTIES = [ 
    "Cardiologia", "Dermatologia", "Ginecologia", "Pediatria", "Ortopedia", "Oftalmologia" 
] 
 
def init_db(db: Session): 
    # 1. Criar Cidades 
    for city_data in CITIES: 
        city = db.query(models.City).filter(models.City.name == city_data["name"]).first() 
        if not city: 
            db_city = models.City(**city_data) 
            db.add(db_city) 
    db.commit() 
 
    # 2. Criar Especialidades 
    for spec_name in SPECIALTIES: 
        spec = db.query(models.Specialty).filter(models.Specialty.name == spec_name).first() 
        if not spec: 
            db_spec = models.Specialty(name=spec_name) 
            db.add(db_spec) 
    db.commit() 
 
    # 3. Criar Usuario Admin Padrao 
    user = crud_user.get_user_by_email(db, email="admin@cademeumedico.com") 
    if not user: 
        user_in = user_schema.UserCreate( 
            email="admin@cademeumedico.com", 
            password="supersecretadminpassword", 
            full_name="Admin Principal" 
        ) 
        user = crud_user.create_user(db, user_in) 
        user.role = models.UserRole.admin # Define como Admin apos a criacao 
        db.add(user) 
        db.commit() 
 
if __name__ == "__main__": 
    db = SessionLocal() 
    init_db(db) 
    db.close() 
    print("Dados iniciais (Cidades, Especialidades e Admin) criados com sucesso!") 
