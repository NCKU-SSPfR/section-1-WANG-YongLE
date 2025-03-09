from fastapi import Request, HTTPException,Response
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from .operation import get_latest_game_state, move_location, reset_game_state  

router = APIRouter(
    tags=["game"],
    responses={404: {"description": "Not found"}},
)

@router.get("/api/v1/maze")
async def get_maze(username: str):
    """获取当前迷宫数据"""
    game_state = get_latest_game_state(username)
    if game_state is None:
        raise HTTPException(status_code=404, detail="Maze data not found")
    return JSONResponse(game_state)

@router.post("/api/v1/move")
async def move(request: Request):
    """Move player based on direction"""
    body = await request.json()
    username = body.get("username")  # Get username from request
    direction = body.get("direction", "")

    # Get latest game state for the user
    game_state = get_latest_game_state(username)
    if not game_state:
        return JSONResponse({"message": "User does not exist, please create an account first", "status": 0}, status_code=400)

    game_state = move_location(game_state, direction)

    return JSONResponse(game_state)

@router.get("/api/v1/reset")
async def reset_game(response: Response,username: str):
    """Reset game state"""
    reset_game_state(username)
    return JSONResponse(get_latest_game_state(username))