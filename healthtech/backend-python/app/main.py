from fastapi import FastAPI

from app.api.analyze import router as analyze_router

app = FastAPI(title="Pharmacogenomics Engine", version="1.0.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(analyze_router)
