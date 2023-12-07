## Installing and Running

To start app you need to have .env file with variables in the root path of project.

> pip install -r requirements.txt

> cd article_api/

> python manage.py runserver


App running!


## Endpoints

- **POST** /api/articles_info/
- Body **POST** {"file": *.xlsx} or {"article": \<int\>}

## Response

```json
[
    {
        "article": 123456,
        "brand": "Some brand",
        "title": "Card title"
    }
]
```