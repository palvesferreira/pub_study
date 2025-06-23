from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import app.models.ativo
from app.api.deps import get_db

router = APIRouter()

@router.post("/ativos/", response_model=app.models.ativo.Ativo)
async def criar_ativo(ativo: schemas.AtivoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.criar_ativo(db, ativo)

@router.get("/ativos/", response_model=list[app.models.ativo.Ativo])
async def listar_ativos(db: AsyncSession = Depends(get_db)):
    return await crud.listar_ativos(db)