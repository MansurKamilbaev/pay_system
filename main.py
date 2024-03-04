from fastapi import FastAPI

from card.card_api import card_router

# Для html
from starlette.templating import Jinja2Templates

from currency.currency_api import currency_router

from transfer.transfers_api import trans_router
from users.user_api import user_router

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

# Если хотите выводить html странички
template = Jinja2Templates(directory='templates')

from html_example.html_show import html_router

app.include_router(html_router)

app.include_router(card_router)
app.include_router(user_router)
app.include_router(trans_router)
app.include_router(currency_router)
