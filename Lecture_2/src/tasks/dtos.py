from pydantic import BaseModel

class TaskSchema(BaseModel):
    title : str
    description : str
    is_completed : bool = False

# ============= Response ============
class TaskResponseSchema(BaseModel):
    id:int
    title : str
    description : str
    is_completed : bool

# ----- Task Complete Schema ----
class TaskComplete(BaseModel):
    is_completed : bool 