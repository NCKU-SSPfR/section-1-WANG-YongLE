from fastapi import FastAPI, Request, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from .database.initialize import initialize

from .auth.router import router as auth_router
from .game.router import router as game_router
import uvicorn
app = FastAPI()
app.include_router(auth_router)
app.include_router(game_router)
initialize()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
