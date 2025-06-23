from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud import title_crud
from app.schemas import TitleCreate, Title
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=Title)
async def create_title(title: TitleCreate, db: AsyncSession = Depends(get_db)):
    return await title_crud.create_title(db, title)

@router.get("/", response_model=list[Title])
async def read_titles(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await title_crud.get_titles(db, skip=skip, limit=limit)