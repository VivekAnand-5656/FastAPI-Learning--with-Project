from fastapi import Request, status, HTTPException,Depends
from src.utills.settings import setting
from sqlalchemy.orm import Session
import jwt
from src.users.models import UserModel
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from src.utills.db import get_db


# ----- TOKEN Send ---------
def is_authorized(request:Request, db:Session=Depends(get_db)):
    try:
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorazition header missing")
        token = token.split(" ")[-1]
        data = jwt.decode(token, setting.SECRET_KEY, setting.ALGORITHM)
        user_id = data.get("_id")
        
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are Unauthorized")
        
        print(data)
        return {
            "id":user.id,
            "token":token
        }
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Expired")
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")