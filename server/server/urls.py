from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework import routers
from instagram.views import *

# Add the logout view later
# from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
# Public API
router.register(r'comments', CommentView, 'comment')
router.register(r'profiles', ProfilePublicView, 'profile')
router.register(r'stories', UserStoryView, 'story')
router.register(r'postedimages', PostedImageView, 'postedimage')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Custom paths
    re_path(r'^api/postedimages/hashtag/(?P<hashtag>.+)$',
            PostedImageView.as_view({'get': 'get_feed_from_hashtag'})),
    re_path(r'^api/profiles/username/(?P<username>.+)$',
            ProfilePublicView.as_view({'get': 'get_by_username'})),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('oauth/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
