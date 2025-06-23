from sqlalchemy.ext.asyncio import AsyncSession

from app.models import WeeklyQuote
from app.schemas import WeeklyQuoteCreate


async def create_quote(db: AsyncSession, quote: WeeklyQuoteCreate):
    db_quote = WeeklyQuote(**quote.dict())
    db.add(db_quote)
    await db.commit()
    await db.refresh(db_quote)
    return db_quote