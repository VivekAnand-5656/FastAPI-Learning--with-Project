from pydantic import BaseModel

class UserSchema(BaseModel):
    name : str
    username : str
    password : str
    email : str

# ----- Response -----
class UserResponse(BaseModel):
    id : int
    name : str 
    username : str 
    email : str

# ---------- Login Schema -------
class LoginSchema(BaseModel):
    username : str
    password : str

# --------- Login Response -----
class LoginResponse(BaseModel):
    id: int
    token: str