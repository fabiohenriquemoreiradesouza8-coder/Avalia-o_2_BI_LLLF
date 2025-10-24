from sqlalchemy.orm import Session 
from app.db import models 
from app.schemas import user as user_schema 
from app.core.security import get_password_hash 
 
    return db.query(models.User).filter(models.User.email == email).first() 
 
def create_user(db: Session, user: user_schema.UserCreate) -
    hashed_password = get_password_hash(user.password) 
    db_user = models.User( 
        email=user.email, 
        full_name=user.full_name, 
        hashed_password=hashed_password, 
        role="user" 
    ) 
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user) 
    return db_user 
 
def update_user(db: Session, db_user: models.User, user_in: user_schema.UserUpdate) -
    update_data = user_in.model_dump(exclude_unset=True) 
 
    if "password" in update_data: 
        hashed_password = get_password_hash(update_data["password"]) 
        db_user.hashed_password = hashed_password 
        del update_data["password"] 
 
    for field, value in update_data.items(): 
        setattr(db_user, field, value) 
 
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user) 
    return db_user 
