from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from app.schemas import user as user_schema 
from app.crud import crud_user 
from app.api.v1 import deps 
from app.db import models 
 
router = APIRouter() 
 
@router.get("/me", response_model=user_schema.User) 
def read_users_me( 
    current_user: models.User = Depends(deps.get_current_user), 
): 
    Obtem os dados do usuario autenticado. 
    return current_user 
 
@router.put("/me", response_model=user_schema.User) 
def update_user_me( 
    *, 
    db: Session = Depends(deps.get_db), 
    user_in: user_schema.UserUpdate, 
    current_user: models.User = Depends(deps.get_current_user), 
): 
    Atualiza os dados do usuario autenticado. 
    if user_in.email: 
        existing_user = crud_user.get_user_by_email(db, email=user_in.email) 
        if existing_user and existing_user.id != current_user.id: 
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email ja em uso.") 
 
    user = crud_user.update_user(db=db, db_user=current_user, user_in=user_in) 
    return user 
