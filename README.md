# database_models
database models in different containers, making use of docker-compose mounting images for cassandra and redis


model cassandra

We build a docker image with the configurations stored in the .yml file

### On Linux and Mac
```sudo docker-compose up -d```

### On windows
```docker-compose up -d```

```docker exec -it ID-CONTAINER redis-cli ```
