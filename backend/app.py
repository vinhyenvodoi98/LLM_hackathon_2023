from fastapi import FastAPI

from routes.technology import router as technology_router
from routes.analysis import router as analysis_router

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(
    technology_router,
    tags=["Technology Types"],
    prefix="/technology_types",
    dependencies=[],
)


app.include_router(
    analysis_router,
    tags=["Analysis"],
    prefix="/analysis",
    dependencies=[],
)
