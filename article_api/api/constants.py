from pydantic import BaseModel


XLSX_CONTENT_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
CARD_API_URL_TEMPLATE = 'https://card.wb.ru/cards/v1/detail?nm={article}'


class Item(BaseModel):
    article: int
    brand: str = None
    title: str = "not found"
