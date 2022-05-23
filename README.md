# yamdb_final

[![Python](https://img.shields.io/badge/Made%20with-Python-green?logo=python&logoColor=white&color)](https://www.python.org/)
[![Docker](https://img.shields.io/static/v1?message=docker&logo=docker&labelColor=5c5c5c&color=002c66&logoColor=white&label=%20&style=plastic)](https://www.docker.com/)
[![Django](https://img.shields.io/static/v1?message=django&logo=django&labelColor=5c5c5c&color=0c4b33&logoColor=white&label=%20&style=plastic)](https://www.djangoproject.com/)
[![Nginx](https://img.shields.io/static/v1?message=nginx&logo=nginx&labelColor=5c5c5c&color=009900&logoColor=white&label=%20&style=plastic)](https://nginx.org/)
[![Postgres](https://img.shields.io/static/v1?message=postgresql&logo=postgresql&labelColor=5c5c5c&color=1182c3&logoColor=white&label=%20&style=plastic)](https://www.postgresql.org/)
![yamdb_workflow](https://github.com/elityaev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Краткое описание проекта
yamdb_final - приложения в котором можно оставлять отзывы и оценивать 
произведения в различных категориях и жанрах, а также комментировать такие отзывы. 
Для приложения настроены CI(Continuous Integration) и CD (Continuous Deployment), 
благодаря чему при внесении изменений в главную (main) ветку проекта 
выполняется следующий функционал:
* проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) 
и запуск pytest из репозитория yamdb_final;
* сборка и доставка докер-образа для контейнера web на Docker Hub;
* автоматический деплой проекта на боевой сервер;
* отправка уведомления в Telegram о том, что процесс деплоя успешно завершился.


### Запуск проекта

После клонирования проекта необходимо cкопировать `.env.example` и назвать его `.env`, 
заполнить переменные окружения

#### Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
#### Для деплоя на удаленный сервер необходимо:

* перенести файлы `docker-compose.yaml` и папку `nginx` c файлом `default.conf`
на сервер, выполнив команду
* на github, в настройках репозитория `Secrets` --> `Actions` создать и заполнить переменные окружения:
```
DOCKER_USERNAME # Имя пользователя на Docker Hub;
DOCKER_PASSWORD # Пароль от Docker Hub;
DB_ENGINE # Указать, что работаем с базой данных PostgresQl;
DB_NAME # Имя базы данных;
DB_HOST # Название контейнера базы данных; 
DB_PORT # Порт для подключения к базе данных;
POSTGRES_USER # Логин для подключения к базе данных;
POSTGRES_PASSWORD # Пароль для подключение к базе данных;
USER # Имя пользователя на сервере;
HOST # Публичный IP-адрес сервера;
PASSPHRASE # Указать в том случае, если ssh-ключ защищен фразой-паролем;
SSH_KEY # Приватный ssh-ключ;
TELEGRAM_TO # ID телеграм-аккаунта;
TELEGRAM_TOKEN # Токен телеграм-бота.
```

_Автор
Литяев Евгений_