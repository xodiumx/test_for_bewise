from fastapi import APIRouter

from .schemas import UserCreate, UserRead
from .utils import auth_backend, fastapi_users
from .views import router as views

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(views)
