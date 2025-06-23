from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.crud_investment_titles import create_title
from app.models import InvestmentTitle
from app.schemas import InvestmentTitleCreate, InvestmentTitleResponse

router = APIRouter()

@router.post("/", response_model=InvestmentTitleResponse)
async def create_title(title: InvestmentTitleCreate, db: AsyncSession = Depends(get_db)):
    return await create_title(db, title)

@router.get("/{title_id}", response_model=InvestmentTitleResponse)
async def read_title(title_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(InvestmentTitle).where(InvestmentTitle.id == title_id))
    title = result.scalars().first()
    if not title:
        raise HTTPException(status_code=404, detail="Título não encontrado")
    return title

@router.get("/", response_model=list[InvestmentTitleResponse])
async def read_titles(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(InvestmentTitle).offset(skip).limit(limit))
    return result.scalars().all()