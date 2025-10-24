from fastapi import APIRouter, Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordRequestForm 
from sqlalchemy.orm import Session 
from app.schemas import user as user_schema 
from app.schemas import token as token_schema 
from app.crud import crud_user 
from app.core import security 
from app.api.v1 import deps 
 
router = APIRouter() 
 
@router.post("/register", response_model=user_schema.User, status_code=status.HTTP_201_CREATED) 
def register_user( 
    *, 
    db: Session = Depends(deps.get_db), 
    user_in: user_schema.UserCreate 
): 
    Cadastra um novo usuario. 
    user = crud_user.get_user_by_email(db, email=user_in.email) 
    if user: 
        raise HTTPException( 
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="O email ja esta cadastrado.", 
        ) 
    user = crud_user.create_user(db=db, user=user_in) 
    return user 
 
@router.post("/login", response_model=token_schema.Token) 
def login_for_access_token( 
    db: Session = Depends(deps.get_db), 
    form_data: OAuth2PasswordRequestForm = Depends() 
): 
    OAuth2-compatible login, retorna JWT. 
    user = crud_user.get_user_by_email(db, email=form_data.username) 
    if not user or not security.verify_password(form_data.password, user.hashed_password): 
        raise HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Email ou senha incorretos", 
            headers={"WWW-Authenticate": "Bearer"}, 
        ) 
 
    access_token = security.create_access_token( 
        data={"sub": user.email} 
    ) 
    return {"access_token": access_token, "token_type": "bearer"} 
