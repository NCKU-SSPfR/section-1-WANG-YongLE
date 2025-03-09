from datetime import datetime, timedelta
from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .database.initialize import initialize
from .database.operation import create_user, get_latest_game_state, reset_game_state
from .game.operation import move_location
from .auth.router import router as auth_router
import uvicorn
app = FastAPI()
app.include_router(auth_router)
initialize()

FRONTEND_URL = "http://localhost:8088"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)









if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
