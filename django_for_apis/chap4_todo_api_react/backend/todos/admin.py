from django.contrib import admin

# Register your models here.
from .models import Todo


# class AppnameAdmin(admin.ModelAdmin):
#     fieldsets = [Todo]


# admin.site.register(Todo, AppnameAdmin)
admin.site.register(Todo)
