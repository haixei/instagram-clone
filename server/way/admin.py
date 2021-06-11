from django.contrib import admin
from .models import User, Comment, PostedImage


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'bio', 'created', 'following', 'avatar')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'likes')


class PostedImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'created', 'likes', 'image')


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostedImage, PostedImageAdmin)
