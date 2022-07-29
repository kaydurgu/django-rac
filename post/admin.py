from django.contrib import admin
from .models import Project


admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' )
    list_display_links = ('id', 'title')
    search_fields = ('title')