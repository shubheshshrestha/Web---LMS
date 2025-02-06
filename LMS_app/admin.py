from django.contrib import admin
from .models import Book, BookType, BorrowingRecord, Member, IsMember
from django.contrib.auth.models import Group, User
# Register your models here.

# register Django models with the Django admin interface.
admin.site.register(Book)   # This allow us to manage those models (e.g., create, read, update, delete records) through the admin dashboard.
admin.site.register(BookType)
admin.site.register(BorrowingRecord)
admin.site.register(Member)


