# Project Documentation

This documentation includes all the important information one should know after cloning the application and deciding to build something similar or change it.

**Legend:**

+ [Docker setup](docs.md#docker-set-up)
+ [Client side architecture](docs.md#client-side-architecture)
+ [Server side architecture](docs.md#server-side-architecture)
  + [Django REST Framework](docs.md#django-rest-framework)
  + [Using PostgreSQL](docs.md#using-postgresql)
+ [Deployment guidelines](docs.md#deployment-guidelines)



## Docker set-up

The Docker set-up is very straightforward, all you have to care about is the main docker-compose file and the docker files from client/server folders. We tell Docker to build three images: server, client and db (based on postgres:alpine). All three of them have their code mounted within the container which allows for hot-reloading and data persistence.

One thing that could not be so obvious for people who don't have any experience with the technology, to make sure that the database can be accessed by the server after it launches the wait-for-it.sh file existence is necessary (can be substituted with other methods too). It basically waits for the availability of the port for a specified amount of time. Without it, there must be involved another way for the server to either not launch before postgres (when its not ready to be used yet) or to wait for the port.



## Client side architecture

*Not available yet.*



##  Server side architecture

When it comes to the server side architecture, it's quite clear since we're dependent on how Django, a very opinionated framework, handles things. The structure of the repository will probably resemble what you've seen before. If you don't have any experience with the framework, I recommend checking out this page first. We're working with one application within the project, our Instagram clone and if you created all necessary files mentioned in the project readme, you're most likely good to go. 



#### Django REST Framework

Since the project involves this technology, I thought it could be worth mentioning what it brings into the application and why I decided to use it. Django REST Framework is nothing else than a tool that helps developers easily create API routes which can be monotone. Aside of that it also involves other features like:

- Making the API web browsable
- Serialization that supports ORM and non-ORM data sources
- Customization on many levels



Another big plus of using it is the really good documentation and community support which can greatly speed up the development process. In this project you can see the footprints of the REST framework in the Serializers and Views files.



#### Using PostgreSQL

For the database I decided to use PostgreSQL, one that conforms to the SQL syntax. It's fully handled by Docker since I'm using an already existing image like mentioned before so you don't have to worry about installing anything. The user and the database are created using information from the .env file.



## Deployment guidelines

*Not available yet.*

 

