from django.contrib import admin

from catalog.models import Film, Producer, Genre

admin.site.register(Film)
admin.site.register(Producer)
admin.site.register(Genre)
# Register your models here.
