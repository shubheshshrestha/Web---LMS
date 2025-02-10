from django.contrib import admin
from .models import Book, BookType, BorrowingRecord, Member
from django.contrib.auth.models import Group, User
# Register your models here.

# Register Django models with the Django admin interface.
admin.site.register(Book)   # This allow us to manage those models (e.g.,"CRUD".. create, read, update, delete records) through the admin dashboard.
admin.site.register(BookType)
admin.site.register(BorrowingRecord)
admin.site.register(Member)












# Custom admin class for the Book model
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'category', 'available_copies')  # Fields to display in the list view
#     list_filter = ('category',)  # Add filters for the list view
#     search_fields = ('title', 'author', 'isbn')  # Add search functionality

# # Custom admin class for the BorrowingRecord model
# class BorrowingRecordAdmin(admin.ModelAdmin):
#     list_display = ('book', 'member', 'borrowed_date', 'due_date', 'status')  # Fields to display in the list view
#     list_filter = ('status',)  # Add filters for the list view
#     search_fields = ('book__title', 'member__full_name')  # Add search functionality

# # Register models with custom admin classes
# admin.site.register(Book, BookAdmin)
# admin.site.register(BorrowingRecord, BorrowingRecordAdmin)