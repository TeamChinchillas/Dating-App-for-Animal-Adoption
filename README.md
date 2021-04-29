# Run the app by Docker
If you run the app for the first time, please run this command.

```
docker-compose up --build
```

Press Ctrl+C to quit


Next time, you just run
```
docker-compose up
```

### How to get into a Docker container
First, check your container id
```
docker ps
```

Then, run the command.
```
docker exec -it {CONTAINER_ID} /bin/bash
```

After connecting to your container, if you want to initialize your DB data, run the following command
```
python animal_adoption/models/initialize_db_data.py 
```
