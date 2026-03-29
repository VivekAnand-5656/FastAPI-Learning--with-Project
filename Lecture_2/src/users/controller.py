from src.users.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.users.models import UserModel
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from src.utills.settings import setting
from datetime import datetime, timedelta
import jwt
password_hash = PasswordHash.recommended()


def get_passsword_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password,hashed_password)  # password bycrypted
# ============ Login ==============
def login(body:LoginSchema,db:Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong username!")
    userpassword = db.query(UserModel).filter(UserModel.hash_password == body.password).first()
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong Password!")
    
    exp_time = datetime.now() + timedelta(minutes=setting.EXP_TIME)
    token = jwt.encode({"_id":user.id, "exp":exp_time}, setting.SECRET_KEY, setting.ALGORITHM)
    
    return {
        "id":user.id,
        "token":token
    }

def register(body:UserSchema, db:Session):
    print("Body: ",body)
    data = body.model_dump()
    exist_email = db.query(UserModel).filter(
        UserModel.email == data["email"] 
    ).first()

    exist_username = db.query(UserModel).filter(
        UserModel.username == data["username"]
    ).first()

    if exist_email:
        raise HTTPException(status_code=400, detail="Email already exist!")
    elif exist_username:
        raise HTTPException(status_code=400, detail="Choose Different Username!")
    
    hash_password = get_passsword_hash(data["password"])
    new_user = UserModel (
        name = data["name"],
        username = data["username"],
        hash_password = hash_password,
        email = data["email"]
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user