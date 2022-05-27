# social_ntw
### Описание:
проект социальной сети, с возможностью публиковать посты,
ставить и убирать лайки к постам

тестовое задание

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SergeSGH/social_ntw.git
```
```
cd social_ntw/infra
```

Собрать и запустить контейнеры:
```
docker-compose up -d --build
```
База данных загружается из репозитория (инициализация не нужна).
Проект доступен:
```
http://127.0.0.1/admin/ - админ панель (логин 'admin', пароль 'admin')
http://127.0.0.1/api/ - доступ к API интерфейсу
```
автозаполнение данных пользователя при регистрации:
```
добавление информации о пользователе (location, company) при регистрации
по информации о e-mail с сайта clearbit.com
информация добавляется только если ее нет в исходных данных
```
проверка e-mail:
```
проверка в базе сайта emailhunter.co
добавлена вся необходимая логика, но так как регистрация на emailhunter.co невозможна с почтовым доменом электронной почты,
при регистрации принимаются только адреса с доменом 'gmail.com'
```