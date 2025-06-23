from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.base_class import Base
from app.db.sessions import engine

docs_url = f"{settings.API_V1_STR}/docs" if settings.API_V1_DOCS else None
redoc_url = f"{settings.API_V1_STR}/redoc" if settings.API_V1_REDOC else None
openapi_url = f"{settings.API_V1_STR}/openapi.json" if (settings.API_V1_DOCS or settings.API_V1_REDOC) else None

print(f"""
Using:
    docs_url = {docs_url}
    redoc_url = {redoc_url}
    openapi_url = {openapi_url}
""")

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=openapi_url, docs_url=docs_url, redoc_url=redoc_url,
              # lifespan=lifespan
              )

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],  # -> todo: check if necessary
    )


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # try:
    #     async with engine.begin() as conn:
    #         await conn.run_sync(Base.metadata.create_all)
    # except Exception as exc:
    #     print(f'DATABASE_URL: {settings.DATABASE_URL} -> Connection error {type(exc)} -> {exc}')

app.include_router(api_router, prefix=settings.API_V1_STR)
