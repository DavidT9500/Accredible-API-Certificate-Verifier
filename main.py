from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from api.routes import router as api_router

app = FastAPI(
    title="Accredible API Certificate Verifier",
    version="0.1.0",
    description="Simple FastAPI app to verify Accredible certifications",
    docs_url=None,
    redoc_url=None
)

app.include_router(api_router)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Accredible API Certificate Verifier - Docs"
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title="Accredible API Certificate Verifier - ReDoc"
    )