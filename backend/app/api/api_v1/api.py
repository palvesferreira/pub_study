from fastapi import APIRouter
from .endpoints import users # , institutions # , quotes# , titles # , auth, ativos

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(titles.router, prefix="/titles", tags=["Titles"])
# api_router.include_router(ativos.router, prefix="/ativos", tags=["ativos"])
# api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
# api_router.include_router(institutions.router, prefix="/institutions", tags=["institutions"])
# api_router.include_router(quotes.router, prefix="/quotes", tags=["quotes"])
