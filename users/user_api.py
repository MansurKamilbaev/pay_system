from fastapi import APIRouter
from database.userservice import registration_user_db, edit_user_db, get_exact_user_db, get_all_users_db, delete_user_db,check_user_email_db

from datetime import datetime

from users import UserRegistrationValidator, EditUserValidator

user_router = APIRouter(prefix='/user', tags=['Работа с пользователями '])


@user_router.post('/register')
async def register_new_user(data: UserRegistrationValidator):
    new_user_data = data.model_dump()

    checker = check_user_email_db(data.email)

    if checker:
        return {"message": 'Пользователь с таким номером уже есть в БД'}
    else:
        result = registration_user_db(reg_date=datetime.now(), **new_user_data)
        return result


@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {"message": result}
    else:
        return {'message': 'Такого пользователя нет'}


@user_router.put('/edit')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    return result


@user_router.get('/get')
async def get_all_users():
    result = get_all_users_db()

    if result:
        return {"message": result}
    else:
        return {"message": 'Таких пользователей нет'}


@user_router.delete('/delete')
async def get_delete_user(user_id):
    result = delete_user_db(user_id)

    if result:
        return {"message": "Пользователь удален"}
    else:
        return {"message": 'Пользователя нет'}
