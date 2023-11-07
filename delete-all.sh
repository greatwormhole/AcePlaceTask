docker container rm mongodb
docker container rm fastapi

docker volume rm docker_fastapi-data
docker volume rm docker_mongo-log
docker volume rm docker_mongo-data

docker network rm web-app