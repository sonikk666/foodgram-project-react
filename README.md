# Foodgram — программный интерфейс для обмена рецептами

[![CI](https://github.com/sonikk666/foodgram-project-react/actions/workflows/diplom_workflow.yaml/badge.svg?branch=master)](http://51.250.9.36/)

## Описание

Благодаря этому проекту можно находить рецепты приготовления вкусных блюд, делиться своими рецептами. Сохранять рецепты в избранные, а так же автоматически составлять список покупок (ингредиентов) для выбранных рецептов.

### Технологии

- Python 3.7
- Django 2.2.19
- DjangoRestFramework 3.12.4

### Запуск проекта в Docker

- Перейдите в папку infra/ корневого каталога
- Создате файл .env и наполните его по следующему шаблону:

```bash
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

- Выполните по очереди команды:

```bash
# Запуск docker-compose в фоновом режиме
docker compose up -d
# Миграции
docker compose exec backend python manage.py migrate
# Создайте своего суперюзера
docker compose exec backend python manage.py createsuperuser
# Подгрузка статики
docker compose exec backend python manage.py collectstatic --no-input
# Копируем файл с тестовой базой в контейнер
docker cp db.json nikita-backend-1:/app/
# Заполние базы данных
docker compose exec backend python manage.py loaddata ../data/db.json
# Для остановки контейнеров воспользуйтесь командой
docker compose down -v
```

### Описание эндпоинтов

Запросы к API начинаются с /api/ ```api```

<!-- В разработке -->

### Автор

- Никита Михайлов
