from fastapi import Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordBearer 
from sqlalchemy.orm import Session 
from app.db.session import get_db 
from app.db import models 
from app.core import security 
from app.crud import crud_user 
 
# URL para onde o cliente envia o 'username' e 'password' 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login") 
 
def get_current_user( 
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme) 
) -
    Decodifica o token JWT para obter o usuario atual. 
    credentials_exception = HTTPException( 
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Nao foi possivel validar as credenciais", 
        headers={"WWW-Authenticate": "Bearer"}, 
    ) 
 
    email = security.decode_access_token(token=token) 
    if email is None: 
        raise credentials_exception 
 
    user = crud_user.get_user_by_email(db, email=email) 
    if user is None: 
        raise credentials_exception 
 
    return user 
 
def get_current_admin_user( 
    current_user: models.User = Depends(get_current_user), 
) -
    Verifica se o usuario atual e um administrador. 
    if current_user.role != "admin": 
        raise HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Recurso restrito a administradores" 
        ) 
    return current_user 
