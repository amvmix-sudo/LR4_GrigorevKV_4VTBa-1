def get_users():
    """
    Возвращает список пользователей.
    """
    return [
        {"id": 1, "username": "user1", "email": "user1@example.com"},
        {"id": 2, "username": "user2", "email": "user2@example.com"},
    ]


def create_user(username, email):
    """
    Создаёт нового пользователя.
    """
    return {
        "id": 3,
        "username": username,
        "email": email,
    }
