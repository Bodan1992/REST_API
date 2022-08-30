from voluptuous import Schema


single_user = Schema({
    "data": {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    "support": {
        "url": str,
        "text": str
    }
})

create = Schema({
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str
})


register = Schema({
    "id": int,
    "token": str
})


list_user = Schema(
{
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": [
        {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
    ],
    "support": {
        "url": str,
        "text": str
    }
})
