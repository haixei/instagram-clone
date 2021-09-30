![In works](https://i.imgur.com/eVFsNyu.png)

# Instagram Clone

This project is a full-stack application made with Django and Vue that imitates Instagram. It allows people to post messages and stories, follow users, write comments and "like" content. This repository contains all the code needed right with the instructions on how to use it as well as explanations for different parts of it.



- [*Documentation*](https://github.com/haixei/instagram-clone/blob/master/docs/docs.md)
- [*Developer API reference*](https://haixei.github.io/instagram-clone/)
- *Live website (in development)* 🛠



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



## Contribute

This project serves only an educational purpose, but contributions related to improving the quality of the code are very much welcome. The app in the future could serve as a resource for people who want to learn more about Django or Vue.

