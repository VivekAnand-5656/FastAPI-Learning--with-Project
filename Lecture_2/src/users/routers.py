from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.utills.db import get_db
from src.users import controller
from src.users.dtos import UserSchema, UserResponse, LoginSchema, LoginResponse

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model=UserResponse , status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controller.register(body,db)

# ------ Login -----
@user_routes.post("/login",response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controller.login(body,db)