# meet2code
meet2code - веб-приложения для поиска коллег по работе над определенными проктами.

Проект реализован на веб-фреймворке Django.

Чтобы запустить проект, необходимо сделать следующее:
- установить Docker (https://docs.docker.com/get-docker/)
- установить архив с проектом
- запустить следующие команды в PowerShell:
```
py install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
docker run -p 6379:6379 -d redis:5
py manage.py runserver
```
- перейти на:
```
127.0.0.1:8000
```
