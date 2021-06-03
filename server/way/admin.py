from django.contrib import admin
from .models import User, Comment, PostedImage


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'bio', 'created', 'following')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author')


class PostedImageAdmin(admin.ModelAdmin):
    list_display = ('imgURL', 'description', 'created')


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostedImage, PostedImageAdmin)
