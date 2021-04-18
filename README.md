# meet2code
Многие люди, которые интересуются программированием, в тот или иной момент времени задумывались о том, чтобы поработать в команде над каким-либо проектом. Однако зачастую проблема как-раз таки заключалась в подборе команды и поиске единомышленников. Желая решить эту проблему, мы решили создать meet2code.

meet2code - веб-приложение для поиска коллег по работе над определенными проектами.

Интеграция пользователя с meet2code бдет происходить следущим образом: регистрация -> заполнение своих личных данных (имя, фамилия, фото, страна, возраст, ссылки на социальные сети) и биографии (в которой указываются предпочтения пользователя, его личные интересы и технологии, которыми он владеет) -> создание своего проекта или присоединение к уже существующему.

При создании проекта пользователь может указать его перспективы, проблемы, которые он намеревается решить, а также какого рода специалисты ему требуются. Если кто-нибудь заинтересуется в участии в этом проекте, он сможет отправить заявку в друзья к создателю проекта, затем связаться с ним во встроенном приватном чате. Если создатель проекта будет удовлетворен поступившей заявкой, то он сможет добавить этого человека в проект как участника. Будучи участником проекта, пользователь займет одну из ролей специалиста, которые были нужны в данном проекте. В самой странице проекта его участникам будет доступен групповой чат, где они могут делиться своими мыслями по поводу проекта, сниппетами кода.

Проект реализован на веб-фреймворке Django.

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

