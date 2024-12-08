from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("/")
async def sign_in():
    pass