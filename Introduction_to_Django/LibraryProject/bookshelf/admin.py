from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns
    search_fields = ('title', 'author')                     # Enable search box
    list_filter = ('publication_year',)                     # Add filter sidebar
