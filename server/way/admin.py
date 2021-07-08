from django.contrib import admin
from .models import User, Comment, PostedImage, UserStory


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('following',)
    list_display = ('username', 'bio', 'created', 'avatar')


class CommentAdmin(admin.ModelAdmin):
    filter_horizontal = ('likes',)
    list_display = ('content', 'author')


class PostedImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('likes',)
    list_display = ('description', 'created', 'image')


class UserStoryAdmin(admin.ModelAdmin):
    list_display = ('created', 'author', 'image')


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostedImage, PostedImageAdmin)
admin.site.register(UserStory, UserStoryAdmin)
