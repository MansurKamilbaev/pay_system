from database.models import User
from database import get_db

from datetime import datetime


def registration_user_db(name, surname, phone_number, email, city, reg_date, password):
    db = next(get_db())

    new_user = User(name=name, surname=surname, phone_number=phone_number, email=email,
                    city=city, reg_date=reg_date, password=password)

    db.add(new_user)
    db.commit()

    return 'Пользователь успешно зарегался брат!'


def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return 'Я хз брат!'


def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users


def check_user_email_db(email):
    db = next((get_db()))

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return checker
    else:
        return 'Нет такого emaila!'


def edit_user_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_info == 'email':
            exact_user.email = new_info
        elif edit_info == 'city':
            exact_user.city = new_info

        db.commit()

        return 'Данные успешно изменены'
    else:
        return 'Такой пользователь отсуствует'

# def delete_user_db():


