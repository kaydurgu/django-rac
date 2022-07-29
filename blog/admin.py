
from django.contrib import admin
from .models import Blog, Comment, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    '''
    fieldsets = [
        (None, {'fields' : ['title']})
    ]
    '''
    inlines = [CommentInline]
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

