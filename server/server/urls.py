from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from way.views import *
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# Add the logout view later
# from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
router.register(r'comments', CommentView, 'comment')
router.register(r'profiles', ProfileView, 'profile')
router.register(r'userstories', UserStoryView, 'userstory')
router.register(r'postedimages', PostedImageView, 'postedimage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Custom paths
    re_path(r'^api/postedimages/getFeed/(?P<username>.+)$',
            PostedImageView.as_view({'get': 'get_feed'})),
    re_path(r'^api/postedimages/hashtag/(?P<hashtag>.+)$',
            PostedImageView.as_view({'get': 'get_feed_from_hashtag'})),
    re_path(r'^api/userstories/username/(?P<username>.+)$',
            UserStoryView.as_view({'get': 'get_stories'})),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('oauth/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
