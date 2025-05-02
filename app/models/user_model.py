from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username: str = Field(index=True)
    email: str

class User(UserBase, table=True):
    id: int | None = Field(primary_key=True, default=None)
    password: str
    
class UserCreate(UserBase):
    password: str
    
class UserPublic(UserBase):
    id: int
    