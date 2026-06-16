from fastapi import APIRouter

router=APIRouter()


@router.get('/check')
def check():
    return{"messages":"check query working"}