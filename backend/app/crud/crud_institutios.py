from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Institution


async def get_institution_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Institution).where(Institution.name == name))
    return result.scalars().first()

async def create_institution(db: AsyncSession, name: str):
    db_inst = Institution(name=name)
    db.add(db_inst)
    await db.commit()
    await db.refresh(db_inst)
    return db_inst
