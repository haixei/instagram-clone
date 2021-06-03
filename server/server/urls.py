from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ..way import views

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'user')
router.register(r'comments', views.CommentView, 'comment')
router.register(r'postedimages', views.UserView, 'postedimage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]