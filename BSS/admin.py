from django.contrib import admin
from .models import Available_Books,Available_Stationary,Total_books

# Register your models here.
admin.site.register(Available_Books)
admin.site.register(Available_Stationary)
admin.site.register(Total_books)