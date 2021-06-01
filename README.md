# meet2code

Чтобы запустить проект, необходимо сделать следующее:
- установить Docker (https://docs.docker.com/get-docker/)
- установить архив с проектом
- запустить следующие команды в PowerShell:
```
pip install -r requirements.txt
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

