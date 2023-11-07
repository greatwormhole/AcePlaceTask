# AcePlaceTask

- Переменные окружения задаются в ./docker/environments/ <br />
Соответственно db.env контролирует переменные для работы базы данных, а backend.env - WEB приложение
- Для запуска приложения необходимо клонировать репозиторий и из корневой папки репозитория выполнить запустить bash файл командой: 
```bash
bash launch.sh
```
- Реализованы следующие endpoints: POST /create, GET /list, POST /read
- Протестировать отправку запросов можно через http://localhost:8000/docs/ после запуска сервиса вышеупомянутой командой bash. Примеры запросов:<br />
```bash
curl -X 'POST' \
  'http://localhost:8000/create/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": <userId>,
  "key": "registration",
  "target_id": null,
  "data": {}
}'
```
```bash
curl -X 'GET' 'http://localhost:8000/list/?user_id=<userId>&skip=2&limit=3'
```
```bash
curl -X 'POST' \
  'http://localhost:8000/read/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": "2f742043-20be-4102-984f-d13b50ac6682",
  "notification_id": "654aa405f92cf0104eb48658"
}'
```
Примеры ответов:
```json
{"success":false,"msg":"User not found"}
``````
```json
{
    "success": true, 
    "data": {
        "elements": 4, 
        "new": 3, 
        "request": {
            "user_id": "2f742043-20be-4102-984f-d13b50ac6682", 
            "skip": 0, 
            "limit": 5}, 
        "list": [
            {
                "id": "654aa402f92cf0104eb48657", 
                "timestamp": 1699390466, 
                "is_new": true, 
                "user_id": "2f742043-20be-4102-984f-d13b50ac6682", 
                "key": "new_post", 
                "target_id": null, 
                "data": {"123": 123}}, 
            {
                "id": "654aa405f92cf0104eb48658", 
                "timestamp": 1699390469, 
                "is_new": true, 
                "user_id": "2f742043-20be-4102-984f-d13b50ac6682", 
                "key": "new_post", 
                "target_id": null, 
                "data": {"123": 123}}, 
            {
                "id": "654aa405f92cf0104eb48659", 
                "timestamp": 1699390469, 
                "is_new": true, 
                "user_id": "2f742043-20be-4102-984f-d13b50ac6682", 
                "key": "new_post", 
                "target_id": null, 
                "data": {"123": 123}}, 
            {
                "id": "654aa406f92cf0104eb4865a", 
                "timestamp": 1699390470,
                "is_new": false, 
                "user_id": "2f742043-20be-4102-984f-d13b50ac6682", 
                "key": "new_post", 
                "target_id": null, 
                "data": {"123": 123}
            }
        ]
    }
}
```
```json
{"success":true}
```
Пример email'ов:
![txt](https://github.com/greatwormhole/AcePlaceTask/blob/main/123.png)
- Конфиг веб-приложения может быть найден в ./backend/conf.py; Там же обозначены Ограничение на количество уведомлений, а также дефолтные параметры для GET запросы и конфиги для запуска SMTP и сервера через uvicorn
- Для создания WEB-интерфейса использован фреймворк FastAPI + Motor (Асинхронное расширение для PyMongo) для подключения к MongoDB в контейнере (По умолчанию, занимаются порты 8000 для веб-приложения и 27017 для базы данных, а также 465 для SMTP)
- Для отправки email использовался сервис Яндекса smtp.yandex.ru
- Сервис запускался в WSL2 с образом Ubuntu 20.04
- Для очистки содержимого и удаления контейнеров запустите 
```bash
bash delete-all.sh
```