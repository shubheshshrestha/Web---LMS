from rest_framework import serializers
from datetime import date
from .models import BorrowingRecord, Book, BookType, Member
from django.contrib.auth.models import Group, User
# from .models import User

class BorrowingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowingRecord
        fields = '__all__'

    def validate(self, data):
        today = date.today()
        if data.get('returned_date'):
            data['status'] = 'returned'
        elif data['due_date'] < today:
            data['status'] = 'overdue'
        else:
            data['status'] = 'borrowed'
        return data
    
class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username","password","groups"]
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "email": {
                "required": True
            },
            "username": {
                "required": True
            }
        }

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        read_only_fields = ["membership_id"] # Can't change membership_id(user) when editing.

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


