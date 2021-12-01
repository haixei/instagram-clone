# Back-end documentation

1. [Overview of the application](#1-overview-of-the-application)
2. [Using docker](#2-using-docker)
3. [Django REST Framework](#3-using-docker)
4. [PostgreSQL](#4-postgresql)
5. [OAuth](#5-oauth)
6. [Additional in-code documentation](#6-additional-in-code-documentation)
7. [Deployment](#7-deployment) ✍️



## 1. Overview of the application

The back-end of the project mainly serves a purpose of an API. Django was chosen as the framework because of how opinionated and structured it is. It's a perfect choice in a project like this where we can expect a lot of new features in the future and consistency is the key for a comfortable development process. Django also comes with a lot of helpful libraries that solve a lot of common issues for us. It should also be mentioned that the whole project is dockerized.



#### Prerequisites

This documentation assumes that you already comfortable with Python and have some experience developing Django applications. If you lack with the latter, [this link](https://www.djangoproject.com/start/) will take you to the starting guide in its documentation. The rest of the architecture is based on the [Django REST Framework](https://www.django-rest-framework.org/) that is quite easy to understand once you get a hang of what each file is responsible for. 



#### Where to start?

If you follow all the instructions from the project's README file, you are good to go. After you run the application, your adventure within it shouldn't be confusing. The structure of it is very basic and only spiced up a bit with the additional libraries which is covered later in the documentation.



## 2. Using Docker

*"But it runs on my PC! Well.. let's just ship my PC."*

Docker is an open source containerization platform and is used in this project to create separate environments for parts of the application. To understand how it works, please visit this link. It's also important that you understand the concept of images and volume mounting, all of which are used for this project.



## 3. Django REST Framework

Django REST Framework is a go-to way to creating REST API's in Django. It creates a nice structure for basic functionality that one can also easily modify in special cases. Creating API's can be monotone, but with DRF things like registering and generating routes is done automatically. To create a new view, all you have to do is to create a model that will represent the database schema, a serializer that will take care of processing response data and a view that will create all necessary routes.

[Here](https://www.django-rest-framework.org/tutorial/quickstart/) you can see a simple example of how it can be used in practice. In our project, the architecture of it looks basically the same. The only difference is the presence of the customviewsets.py that allows you to create a custom set of routes that should be available in the API (ex. if you don't want to allow to create new instances, so remove the POST request) , the permissions.py that defines who is allowed to access specific routes and custommixins.py, a way to reuse route behavior.



#### Examples

```python
# customviewsets.py
# This custom view set allows only update and delete routes,
# all other ones like retrieve or list are going to return
# status code 405 (Bad Request)
class UpdateDestroyViewSet(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass
```

```python
# permissions.py
# This custom permission makes sure that only the owner of
# an instance is allowed to modify it
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            return obj.author == request.user
        except AttributeError:
            return obj.user == request.user

```

```python
# custommixins.py
# This custom mixin will overwrite the default behavior of the
# create route if applied
class CreateAuthorization:
    def create(self, request, *args, **kwargs):
        # Allow access only to people who are currently logged in
        if request.session.session_key is not None:
            # If the image author matches the logged in user, proceed with creation
            session = Session.objects.get(session_key=request.session.session_key)
            session_data = session.get_decoded()
            uid = session_data.get('_auth_user_id')
            if uid == request.data['author']:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=201, headers=headers)
            else:
                return Response('You are not authorized to post for that user.', 									status=403)
        else:
            return Response('Log in to post.', status=403)
```



#### Custom routes

Sometimes there is a need for more customization or additional routes. In this scenario refer to this part of DRF documentation that covers this topic. Below we can see an example from the project.

```python
# Custom route for a posted image view
@action(detail=False, methods=['GET'], name='feed')
    def feed(self, request):
        if request.session.session_key is not None:
            session = Session.objects.get(session_key=request.session.session_key)
            session_data = session.get_decoded()
            uid = session_data.get('_auth_user_id')

            profile = Profile.objects.get(user_id=uid)
            followed = profile.following.values_list('username', flat=True)
            images = PostedImage.objects.filter(author__username__in=followed)
            serializer = self.serializer_class(images, many=True)
            return Response(serializer.data)
        else:
            return Response('Log in to see your feed.',
                            status=403)
        
# All we did was adding the @action decorator and returning a serialized response, now you can access this route as /api/postedimages/feed/
```

In a situation where we also want the route to have a parameter passed to it, we write it in the following way:

```python
# views.py
def get_feed_from_hashtag(self, request, hashtag):
	images = PostedImage.objects.filter(hashtags__icontains=hashtag)
	serializer = self.serializer_class(images, many=True)
	return Response(serializer.data)


# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Custom paths
    re_path(r'^api/postedimages/hashtag/(?P<hashtag>.+)$',
            PostedImageView.as_view({'get': 'get_feed_from_hashtag'})),
# (...)
```



#### Admin site & browsing the API

DRF also allows you to use the admin dashboard where you can look-up data and create or delete new instances of it. To log in to the admin site you need to use your superuser credentials. You can access the admin page at /admin and the API browser at /api. 

If a model is not exposed to the admin dashboard yet, you might need to check if you added it to the admin.py file, below you can see an example using the Profile model.

```python
# admin.py
from django.contrib import admin
from .models import Profile, Comment, PostedImage, UserStory


class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('following',)
    list_display = ('username', 'bio', 'created', 'avatar')

    
# (...)
admin.site.register(Profile, ProfileAdmin)
```



## 4. PostgreSQL

This project is using PostgreSQL database, it's SQL syntax conforming and highly stable, backed by more than 20 years of development. Docker is using an official image of it, so you don't have to worry about installation. The user and the database are created using information from the .env file.



## 5. OAuth

The application does not have a login form included but is using an OAuth to authorize users. At the moment it is using two services, Google and Twitter. For this purpose we use library called [allauth](https://github.com/pennersr/django-allauth).



## 6. Additional in-code documentation

To enrich the API documentation generated with Redoc, I decided to use DRF Spectacular. It's a simple way to describe responses and add more specific messages to the views.

```python
# Example from the library documentation
@extend_schema(
        parameters=[
          QuerySerializer,  # serializer fields are converted to parameters
          OpenApiParameter("nested", QuerySerializer),  # serializer object is converted to a parameter
          OpenApiParameter("queryparam1", OpenApiTypes.UUID, OpenApiParameter.QUERY),
          OpenApiParameter("pk", OpenApiTypes.UUID, OpenApiParameter.PATH), # path variable was overridden
        ],
        request=YourRequestSerializer,
        responses=YourResponseSerializer,
        # more customizations
)
def retrieve(self, request, pk, *args, **kwargs)
# (...)
```



## 7. Deployment

*In works..* ✍️
