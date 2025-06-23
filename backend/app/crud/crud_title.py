from sqlalchemy.future import select
from app.models import InvestmentTitle
from app.schemas import TitleCreate

async def create_title(db: AsyncSession, title: TitleCreate):
    db_title = InvestmentTitle(**title.dict())
    db.add(db_title)
    await db.commit()
    await db.refresh(db_title)
    return db_title

async def get_titles(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(InvestmentTitle).offset(skip).limit(limit))
    return result.scalars().all()