from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']
    list_filter = ['title', 'author']
    search_fields = ['title', 'author']


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['username', 'date_of_birth']


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
