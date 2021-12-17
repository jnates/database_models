# database_models
database models in different containers, making use of docker-compose mounting images for cassandra and redis


model cassandra

We build a docker image with the configurations stored in the .yml file

### On Linux and Mac
```sudo docker-compose up -d```

### On windows
```docker-compose up -d```

### Entering into redis using the docker image

```docker exec -it ID-CONTAINER redis-cli ```

### Entering into cassandra using the docker image

```docker exec -it cassandra_cassandra_1 cqlsh -u cassandra -p cassandra ```
