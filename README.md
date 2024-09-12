# 📚 Бот для записи пациентов

Этот бот предназначен для упрощения регистрации пациентов в системе.

## 📦 Установка

### Запуск с помощью Docker Compose

1. **Убедитесь, что у вас установлен Docker и Docker Compose.** Если они не установлены, следуйте [официальной документации](https://docs.docker.com/get-docker/) для установки.

2. **Клонируйте репозиторий:**
   
   `git clone https://github.com/username/repo-name.git`
   `cd repo-name`
   
3. **Настройте переменные окружения:**
   Создайте файл .env в корневой директории проекта и добавьте следующие строки:
   
   `BOT_TOKEN=your_bot_token_here`
   `DB_USER="your_db_user"`
   `DB_PASSWORD="your_db_password"`
   `DB_NAME="your_db_name"`
   
4. **Запустите проект:**
   
   `docker-compose up -d --build`
   
5. **Остановите проект:**
   Чтобы остановить работающие контейнеры, используйте:
   
   `docker-compose down`
   
### Запуск без Docker

Если вы предпочитаете запускать проект без Docker, выполните следующие шаги:

1. Установите зависимости:
   
   `pip install -r requirements.txt`
   
2. Запустите бота:
   
   `python bot.py`


## ⚙️ Технологии

- **Язык программирования**: Python
- **Библиотека для Telegram**: [Aiogram](https://docs.aiogram.dev/)
- **База данных**: PostgreSQL

