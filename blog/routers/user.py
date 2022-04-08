from fastapi import APIRouter,  Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
from  .. import database, models, schemas, hashing
from ..repository import user


router = APIRouter(
    prefix = "/user",
    tags = ['Users']
)

get_db = database.get_db
Hash = hashing.Hash()


@router.post('/', response_model = schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    

    return user.create(request, db)

@router.get('/{id}', response_model = schemas.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    
    return user.get_user(id, db)