from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from way.views import *
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', UserView, 'user')
router.register(r'comments', CommentView, 'comment')
router.register(r'postedimages', PostedImageView, 'postedimage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
