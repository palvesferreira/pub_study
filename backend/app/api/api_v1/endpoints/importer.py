from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.core.import_txt import parse_file
from app.models import InvestmentTitle, Institution, WeeklyQuote

router = APIRouter()

@router.post("/txt")
async def import_txt(db: AsyncSession = Depends(get_db)):
    parsed = parse_file("../Pasted_Text_1750534591824.txt")
    for entry in parsed:
        # Buscar ou criar instituição
        institution_result = await db.execute(
            select(Institution).where(Institution.name == entry["institution"])
        )
        institution = institution_result.scalars().first()
        if not institution:
            institution = Institution(name=entry["institution"])
            db.add(institution)
            await db.flush()

        # Criar título
        title = InvestmentTitle(
            code=entry["name"][:50],
            description=f"Automático: {entry['name']}",
            type_title="Renda Fixa",  # pode ser extraído melhor depois
            institution=institution
        )
        db.add(title)
        await db.flush()

        # Criar cotação semanal
        quote = WeeklyQuote(
            date="2025-06-14",
            quantity=1,
            value=entry["value"],
            previous_value=entry["previous_value"],
            gain=entry["gain"],
            gain_percent=entry["gain_percent"],
            title_id=title.id
        )
        db.add(quote)

    await db.commit()
    return {"detail": "Dados importados com sucesso!"}