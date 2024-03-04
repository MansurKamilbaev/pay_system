from fastapi import APIRouter

from database.transervice import create_transaction_db, cancel_transaction_db, get_history_transactions

from transfer import CreateTransactionValidator, CancelTransactionValidator

trans_router = APIRouter(prefix='/transfers', tags=['Транзакции'])


# Запрос на создании транзакции
@trans_router.post('/create')
async def add_new_transaction(data: CreateTransactionValidator):
    transaction_data = data.model_dump()
    result = create_transaction_db(**transaction_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка брат!'}


# Запрос на историю переводов
@trans_router.get('/history')
async def history_transaction(card_id: int):
    result = get_history_transactions(card_from_id=card_id)

    if result:
        return result
    else:
        return {'message': 'Ошибка брат(('}


# Запрос на отмену транзакии
@trans_router.post('/cancel')
async def cancel_transaction(data: CancelTransactionValidator):
    cancel_data = data.model_dump()
    result = cancel_transaction_db(**cancel_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка брат(('}
