![In works](https://i.imgur.com/mkBGAdj.png)
![Web Full-Stack](https://i.imgur.com/meB7aiP.png)

# Instagram Clone

This project is a full-stack application made with Django and Vue that imitates Instagram. It allows people to post messages and stories, follow users, write comments and "like" content. This repository contains all the code needed right with the instructions on how to use it as well as explanations for different parts of it.



## How to start?

Starting the application is quite easy and all we need for this purpose is a Docker installed on your machine. The docker-compose file specifies everything about the start-up of the containers, if you miss anything, look there.



**Step-by-step guide:**

1. Create a .env file with the following contents

```js
POSTGRES_PASSWORD=your_db_password
POSTGRES_USER=your_db_username
POSTGRES_DB=your_db_name
DJANGO_SECRET=django_secret
```

2. Tell Docker to use your profile as the one running the process, this makes sure that your local permissions are working (writing files to folders for example)

   ```dockerfile
   services:
     server:
       (...)
       user: "<your profile id>:<your profile id>"
   ```

3. Start the application using this command

```
docker-compose up -d
```

4. Now you have to migrate your database

+ Enter the database container terminal using this command

  ```
  docker-compose exec server bash
  ```

+ Apply all initial changes to the database

  ```python
  python manage.py makemigrations
  
  # If no errors proceed with the migration
  python manage.py migrate
  ```

5. If all images got build and launched correctly, you should be able to access the client on the port 8080 and the server on the port 8000, next time all you have to do is step 3, **happy coding!**



## Documentation

Despite being quite compact, this project has some things that could be documented for the future users. At the moment the documentation includes the Docker implementation, deployment guide and overview of the architecture.

The documentation files can be find [here.](./docs/docs.md)

