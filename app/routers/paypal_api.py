from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.services.paypal_api_service import generate_access_token
from app.services.paypal_token_storage import set_access_token


security = HTTPBasic()

auth_router = APIRouter(tags=["auth"], prefix="/auth")

@auth_router.post("/login", response_model=dict)
async def generate_access_token_route(credentials: HTTPBasicCredentials = Depends(security)):
    try:
        client_id = credentials.username
        client_secret = credentials.password
        access_token = generate_access_token(client_id, client_secret)
        set_access_token(access_token)
        return {"message": "Access token generated successfully"}
    except Exception as e:
        raise HTTPException(400, str(e))