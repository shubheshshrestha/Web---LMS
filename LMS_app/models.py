from django.db import models
from datetime import datetime, timedelta, date
from django.contrib.auth.models import User, Group, AbstractUser
# from rest_framework.permissions import BasePermission

# Create your models here.

class BookType(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    category = models.ForeignKey(BookType, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    published_date = models.DateField(blank=True, null=True)
    total_copies = models.IntegerField(default=0)
    available_copies = models.IntegerField(default=0)

class Member(models.Model):
    membership_id = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, default="example@example.com")
    phone = models.CharField(max_length=10, default="0000000000")
    address = models.CharField(max_length=255, default="Unknown Address")
    membership_date = models.DateTimeField(auto_now_add=True)
    # is_active_member = models.BooleanField(default=False) # Track active membership

    def __str__(self):
        return f"{self.full_name} ({self.membership_id})"
    
class BorrowingRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue')
    ], default='borrowed')

    def update_status(self):
        today = date.today()

        if self.returned_date:
            self.status = 'returned'
        elif self.due_date < today:
            self.status = 'overdue'
        else:
            self.status = 'borrowed'
        
        self.save()

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"] # This is only required for superuser    

# class MembershipPayment(models.Model):
#     member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="payments")
#     payment_date = models.DateTimeField(auto_now_add=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     valid_until = models.DateTimeField() # Until when the payment is valid

#     def __str__(self):
#         return f"Payment by {self.member.full_name} on {self.payment_date}"