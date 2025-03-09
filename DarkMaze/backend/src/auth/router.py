
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from .cookie import CookieManager
from fastapi import APIRouter
cookieManager=CookieManager()
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
            "status": 0
        })

    create_user(username) 
    cookie = cookieManager.create_cookie("user", username) 
    return JSONResponse({
        "message": "Login successful",
        "cookies": [cookie],
        "status": 1
    })

@router.post("/api/v1/logout")
async def logout(response: Response):
    """Logout and delete Cookie"""
    return JSONResponse({
        "message": "Logout successful",
        "cookies": [],
        "status": 1
    })

