from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.technology import router as technology_router
from routes.analysis import router as analysis_router
from routes.selecting import router as selecting_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


app.include_router(
    selecting_router,
    tags=["Selecting"],
    prefix="/selecting",
    dependencies=[],
)
