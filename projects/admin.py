from django.contrib import admin
from .models import Project, Language, Category
# Register your models here.
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(Project)