from fastapi import FastAPI
from api.auth import router as auth_router

app = FastAPI(title="Book Reservation API", version="1.0.0")
API_PREFIX = "/api/v1"
app.include_router(auth_router, prefix=API_PREFIX + "/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "hiiiii"}