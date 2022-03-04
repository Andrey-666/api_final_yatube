## **Описание и возможности Yatube API:** 

1) Получение списка всех публикаций. 

2) Получение публикации по id. 

3) Создание новой публикации. Запрещены запросы от анонимного пользователя. 

4) Обновление публикации по id. Правами на обновление обладает только автор публикации. Запрещены запросы от анонимного пользователя. 

5) Частичное обновление публикации. Правами на обновление обладает только автор публикации. Запрещены запросы от анонимного пользователя. 

6) Удаление публикации по id. Правами на обновление обладает только автор публикации. Запрещены запросы от анонимного пользователя. 

7) Получение всех комментариев к публикации. 

8) Добавление нового комментария к публикации. Запрещены запросы от анонимного пользователя. 

9) Получение комментария к публикации по id. 

10) Обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Запрещены запросы от анонимного пользователя. 

11) Частичное обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Запрещены запросы от анонимного пользователя. 

12) Удаление комментария к публикации по id. Обновить комментарий может только автор комментария. Запрещены запросы от анонимного пользователя. 

13) Получение списка доступных сообществ. 

14) Получение информации о сообществе по id. 

15) Получение всех подписок пользователя, сделавшего запрос. Запрещены запросы от анонимного пользователя. 

16) Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Запрещены запросы от анонимного пользователя. 

17) Получение JWT-токена. 

18) Обновление JWT-токена. 

19) Проверка JWT-токена. 

 

## Стек технологий:

- Python 3
- Django 2.2
- Djangorestframework
- SimpleJwt
- Gunicorn
- SQLite
- Git
 

## **Как запустить проект:** 

 

### 1) Клонировать репозиторий и перейти в него в командной строке: 

 

git clone https://github.com/Andrey-666/api_final_yatube.git 

 

cd api_final_yatube 

 

### 2) Cоздать и активировать виртуальное окружение: 

 

python3 -m venv venv 

 

source venv/scripts/activate 

 

### 3) Установить зависимости из файла requirements.txt: 

 

python3 -m pip install --upgrade pip 

 

pip install -r requirements.txt 

 

### 4) Выполнить миграции: 

 

python3 manage.py migrate 


***
## Об авторе  
Кузнецов Андрей    
<andrey.66677@yandex.ru>
