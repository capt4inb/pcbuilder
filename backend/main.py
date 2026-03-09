from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import components, builds

app = FastAPI(title="PC Builder API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(components.router)
app.include_router(builds.router)

@app.get("/")
async def root():
    return {"message": "Welcome to PC Builder API"}

