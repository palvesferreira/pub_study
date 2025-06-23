import app.models.ativo
from . import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def criar_ativo(db: AsyncSession, ativo: schemas.AtivoCreate):
    db_ativo = app.models.ativo.Ativo(**ativo.dict())
    db.add(db_ativo)
    await db.commit()
    await db.refresh(db_ativo)
    return db_ativo

async def listar_ativos(db: AsyncSession):
    result = await db.execute(select(app.models.ativo.Ativo))
    return result.scalars().all()