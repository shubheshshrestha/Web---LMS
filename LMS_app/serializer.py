from rest_framework import serializers
from datetime import datetime, timedelta
from .models import BorrowingRecord, Book, BookType, Member
from django.contrib.auth.models import Group, User
# from .models import User

class BorrowingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowingRecord
        fields = '__all__'
        read_only_fields = ["borrowed_date", "status", "due_date"]

    def create(self, validated_data):
        user = self.context["request"].user 
        member = Member.objects.get(membership_id=user)   # Ensure member = Authenticated
        validated_data["member"] = member

        validated_data['due_date'] = datetime.now() + timedelta(days=30)
        return super().create(validated_data)  # calls the create method of the parent class (serializers.ModelSerializer). It handles all the logic for creating the database entry, including saving related fields (like foreign keys).
                                                                                             # Modify -> Create -> Save   



    # def validate(self, data):
    #     today = date.today()
    #     if data.get('returned_date'):
    #         data['status'] = 'returned'
    #     elif data['due_date'] < today:
    #         data['status'] = 'overdue'
    #     else:
    #         data['status'] = 'borrowed'
    #     return data
    
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
        fields = ["full_name", "email", "phone", "address"]
        read_only_fields = ["membership_id"] # Can't change membership_id(user) when editing.

    def create(self, validated_data):
        user = self.context["request"].user  
        validated_data["membership_id"] = user  
        return super().create(validated_data)

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


