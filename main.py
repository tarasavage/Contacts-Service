from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.api.routers import routers
from src.auth.auth_backend import auth_backend
from src.auth.user_manager import get_user_manager
from src.models.users import User
from src.schemas.users import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


for router in routers:
    app.include_router(router)
