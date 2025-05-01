from fastapi import APIRouter
from app.database.db import SessionDep
from app.models.user_model import UserCreate, UserPublic, User
from typing import List
from sqlmodel import select

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)

@router.post('/', response_model=UserPublic)
async def create(user: UserCreate, session: SessionDep) -> UserPublic:  
    db_user = User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
    
    

@router.get('/', response_model=List[UserPublic])
async def findAllUser(session:SessionDep, skip: int = 0, limit: int = 5, ) -> List[UserPublic]:
    statement = select(User).offset(skip).limit(limit)
    results = session.exec(statement).all()
    return results
    
    
    