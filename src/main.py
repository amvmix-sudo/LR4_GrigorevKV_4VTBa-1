"""
Точка входа учебного проекта.
Файл демонстрирует структуру приложения и работу с модулями.
"""

from users import get_users, create_user


def main():
    print("Запуск учебного проекта")

    users = get_users()
    print("Список пользователей:", users)

    new_user = create_user("user3", "user3@example.com")
    print("Создан пользователь:", new_user)


if __name__ == "__main__":
    main()
