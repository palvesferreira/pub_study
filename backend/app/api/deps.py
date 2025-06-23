from app.db.sessions import AsyncSessionLocal


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
