from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from book.models import PrintedBook, AudioBook, Category

admin.site.register(Category, DraggableMPTTAdmin)


# admin.site.register(Profile)


@admin.register(PrintedBook)
class PrintedBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rate')
    search_fields = ('category',)
    fields = ['name', 'image', 'author', 'translator', 'collector', 'publisher', 'category', 'rate', 'volume',
              'book_type',
              'price',
              'year', 'pages', 'is_discount', 'about', 'description']


@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rate')
    search_fields = ('category',)
    fields = ['name', 'image', 'author', 'speaker', 'translator', 'category', 'rate', 'volume', 'book_type', 'price',
              'time', 'is_discount', 'is_transferable', 'about',
              'description']
