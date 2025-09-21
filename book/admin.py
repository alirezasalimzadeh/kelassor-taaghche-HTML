from django.contrib import admin

from book.models import Profile, PrintedBook, AudioBook, Category

admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(PrintedBook)
admin.site.register(AudioBook)
