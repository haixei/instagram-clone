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

For the client side we are using **Vue 3** with a Vuex store to handle state, and we make use of the [Composition API](https://v3.vuejs.org/guide/composition-api-introduction.html) which means that our components use the setup function instead of data, methods etc. Instead of JavaScript I decided to use TypeScript since we do we have support for it and I'm an advocate for strongly typed and strict languages. Even if it can be more time-consuming I believe it's worth it in the end, especially if one works with more people on the project.

We should keep in mind that the newest version of Vue and the support of TypeScript are not fully documented yet and finding information on certain things could be a little bit harder. Since this project is only a proof of concept, I will allow myself to experiment a little bit. For the ease of use, this section in the documentation will explain any non-straightforward concept that one could possibly encounter.



***Currently in works:***

- *Vuex store architecture* ✍️
- *Pages and components*
- *Styling*



##  Server side architecture

When it comes to the server side architecture, it's quite clear since we're dependent on how Django, a very opinionated framework, handles things. The structure of the repository will probably resemble what you've seen before. If you don't have any experience with the framework, I recommend checking out this page first. We're working with one application within the project, our Instagram clone and if you created all necessary files mentioned in the project readme, you're most likely good to go. 



#### Django REST Framework

Since the project involves this technology, I thought it could be worth mentioning what it brings into the application and why I decided to use it. [Django REST Framework](https://www.django-rest-framework.org/) is nothing else than a tool that helps developers easily create API routes which can be monotone. Aside of that it also involves other features like:

- Making the API web browsable
- Serialization that supports ORM and non-ORM data sources
- Customization on many levels



Another big plus of using it is the really good documentation and community support which can greatly speed up the development process. In this project you can see the footprints of the REST framework in the Serializers and Views files.



#### Using PostgreSQL

For the database I decided to use PostgreSQL, one that conforms to the SQL syntax. It's fully handled by Docker since I'm using an already existing image like mentioned before so you don't have to worry about installing anything. The user and the database are created using information from the .env file.



#### The API

The API in our application has a very simple structure thanks for DRF. Some paths got added on top of it following the REST methodology which makes it easy to use for the developers. The full documentation of the API is currently in works and will be published shortly.



## Deployment guidelines

*Not available yet.*

 

