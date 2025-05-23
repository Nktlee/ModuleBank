# 📺 DummyMessenger

**DummyMessenger** — это легкое и быстрое демонстрационное приложение для обмена сообщениями, разработанное на платформе FastAPI и PostgreSQL. Оно создано для изучения основ проектирования RESTful API, работы с асинхронными запросами и обработки данных с использованием асинхронных сессий и репозиториев.

💬 Основное назначение приложения — демонстрировать ключевые аспекты построения API-сервисов на базе Python и технологий микросервисов, включая обработку сообщений, хранение данных и организацию конвейеров обработки запросов.

## 🔧 Особенности приложения

- Поддержка асинхронных запросов и быстрого отклика API.
- Хранение сообщений с использованием базы данных PostgreSQL.
- Репозиторий сообщений с удобной организацией запросов и данных.
- Легковесный и простой клиент для нагружающего тестирования производительности.
- Возможность расширения функционала для собственных экспериментов и исследований.

### 🛠️ Установка и запуск приложения

   Склонируй репозиторий проекта:

   git clone git@github.com:Nktlee/ModuleBank.git

   Запусти приложение с помощью Docker Compose (если у тебя есть Docker):

   ```bash
   docker compose up --build
   ```

   🎯 После успешной сборки и запуска приложения, сервер будет доступен по адресу `http://localhost:8001/messages`.

### 🤝 Работа с приложением

После запуска приложения ты можешь приступить к созданию и управлению сообщениями через HTTP API. Доступны следующие методы:

- **POST `/messages`**: отправка нового сообщения с параметрами (`sender_name`, `text`) и получение последних 10 сообщений (или меньше если не накопилось).

Запуск клиента производится командой python src/client.py
