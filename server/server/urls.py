from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from way.views import *

router = routers.DefaultRouter()
router.register(r'users', UserView, 'user')
router.register(r'comments', CommentView, 'comment')
router.register(r'postedimages', UserView, 'postedimage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]