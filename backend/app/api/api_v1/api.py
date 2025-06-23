from fastapi import APIRouter
from .endpoints import users, auth, importer, institutions, investment_titles, quotes

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(investment_titles.router, prefix="/titles", tags=["Titles"])
api_router.include_router(institutions.router, prefix="/institutions", tags=["institutions"])
api_router.include_router(quotes.router, prefix="/quotes", tags=["quotes"])
api_router.include_router(importer.router, prefix="/import", tags=["Import"])

