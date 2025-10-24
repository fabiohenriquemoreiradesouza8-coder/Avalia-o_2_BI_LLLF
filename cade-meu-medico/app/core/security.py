from datetime import datetime, timedelta, timezone 
from typing import Optional 
from jose import JWTError, jwt 
from passlib.context import CryptContext 
from app.core.config import settings 
 
# Contexto do Passlib para hashing de senhas 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
 
# Algoritmo e Chave Secreta do settings 
ALGORITHM = settings.ALGORITHM 
SECRET_KEY = settings.SECRET_KEY 
 
def verify_password(plain_password: str, hashed_password: str) -
    """Verifica se a senha plana corresponde ao hash.""" 
    return pwd_context.verify(plain_password, hashed_password) 
 
def get_password_hash(password: str) -
    """Gera o hash de uma senha.""" 
    return pwd_context.hash(password) 
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -
    """Cria um novo token JWT.""" 
    to_encode = data.copy() 
    if expires_delta: 
        expire = datetime.now(timezone.utc) + expires_delta 
    else: 
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES) 
 
    to_encode.update({"exp": expire, "iat": datetime.now(timezone.utc)}) 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) 
    return encoded_jwt 
 
def decode_access_token(token: str) -
    """Decodifica um token JWT e retorna o 'sub' (email/username).""" 
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) 
        email: str = payload.get("sub") 
        if email is None: 
            return None 
        return email 
    except JWTError: 
        return None 
