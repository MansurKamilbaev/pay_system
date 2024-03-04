from database.models import UserCard, Transfer
from datetime import datetime

from database import get_db


def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card


def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    checker_card_from = validate_card(card_from, db)
    checker_card_to = validate_card(card_to, db)

    if checker_card_from and checker_card_to:
        if checker_card_from.balance >= amount:
            checker_card_from.balance -= amount

            checker_card_to.balance += amount

            new_transaction = Transfer(card_from_id=checker_card_from.card_id,
                                       card_to_id=checker_card_to.card_id,
                                       amount=amount, transaction_date=datetime.now())

            db.add(new_transaction)
            db.commit()
            return 'Перевод успешно выполнен!'
        else:
            return 'Недостаточно средств на балансе'
    else:
        return f'Одна из карт не существует {checker_card_from}, {checker_card_to}'


def get_history_transactions(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    if card_transaction:
        return card_transaction
    else:
        return 'Нет такой карты'


def cancel_transaction_db(card_from, card_to, amount, transfer_id):
    db = next(get_db())

    checker_card_from = validate_card(card_from, db)
    checker_card_to = validate_card(card_to, db)

    if checker_card_from and checker_card_to:
        transaction_to_cancel = db.query(Transfer).filter_by(transfer_id=transfer_id).first()
        if transaction_to_cancel:
            checker_card_from.balance += amount
            checker_card_to.balance -= amount
            transaction_to_cancel.status = False

            db.delete(transaction_to_cancel)
            db.commit()

            return 'Перевод отменен'
        else:
            return 'Указанный перевод не существует'
    else:
        return f'Одна из карт не существует {checker_card_from}, {checker_card_to}'
    
