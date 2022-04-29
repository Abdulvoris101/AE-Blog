from atexit import register
from django.contrib import admin
from .models import Post, Language, Like, Theme
from django.contrib.admin.decorators import register


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'update_at', 'author')
    list_display = ('id', 'title', )
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display = ('id', 'name', )
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'status')
    list_display_links = ('user', 'post',)
    list_editable = ('status', )

admin.site.register(Theme)