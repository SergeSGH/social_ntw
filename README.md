# social_ntw
### Описание:
проект социальной сети, тестовое задание
с возможностью ставить и убирать лайки

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
Проект доступен:
```
http://127.0.0.1/admin/ - админ панель
http://127.0.0.1/api/ - доступ к API интерфейсу
http://127.0.0.1/swagger/ - документация OpenAPI (swagger)
http://127.0.0.1/redoc/ - документация OpenAPI (ReDoc)
```