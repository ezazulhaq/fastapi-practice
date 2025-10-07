from typing import Annotated
from fastapi import FastAPI
from fastapi import Depends
from sqlmodel import Session

from project3.db.database import get_session

app = FastAPI()

SessionDep = Annotated[Session, Depends(get_session)]
