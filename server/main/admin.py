from atexit import register
from django.contrib import admin
from .models import Post, Category
from django.contrib.admin.decorators import register


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'update_at', 'author')
    list_display = ('id', 'title', )
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
