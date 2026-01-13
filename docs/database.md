# Схема базы данных

## Таблица Users
| Поле | Тип | Описание |
|------|-----|----------|
| id-- | INT | Уникальный идентификатор пользователя |
| username | VARCHAR(50) | Имя пользователя |
| email | VARCHAR(100) | Электронная почта |

## Таблица Requests
| Поле | Тип | Описание |
|-----|----|---------|
| id | INT | Уникальный идентификатор заявки |
| user_id | INT | Идентификатор пользователя |
| text | VARCHAR(255) | Текст заявки |

### SQL-скрипт создания таблиц

```sql
CREATE TABLE Users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE Requests (
    id INT PRIMARY KEY,
    user_id INT,
    text VARCHAR(255)
);
