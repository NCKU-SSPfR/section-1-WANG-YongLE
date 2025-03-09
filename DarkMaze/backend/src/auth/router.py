
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from .cookie import CookieManager
from fastapi import APIRouter
from ..database.operation import create_user  # 确保导入create_user函数
from config import Config
cookieManager = CookieManager()
config=Config()
router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)
@router.post("/api/v1/login")
async def login(request: Request, response: Response):
    """Simulate login, set Cookie"""
    body = await request.json()
    username = body.get("username", "") 

    if(username == ""):
        print("username is null")
        return JSONResponse({
            "message": "Username is empty",
            "cookies": [],
            "status": config.FAILD_STATMENT
        })

    create_user(username) 
    cookie = cookieManager.create_cookie("user", username) 
    return JSONResponse({
        "message": "Login successful",
        "cookies": [cookie],
        "status": config.SUCCESSFUL_STATMENT
    })

@router.post("/api/v1/logout")
async def logout(response: Response):
    """Logout and delete Cookie"""
    return JSONResponse({
        "message": "Logout successful",
        "cookies": [],
        "status": config.SUCCESSFUL_STATMENT
    })

