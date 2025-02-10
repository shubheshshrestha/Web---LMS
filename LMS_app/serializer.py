from rest_framework import serializers
from datetime import datetime, timedelta
from .models import BorrowingRecord, Book, BookType, Member
from django.contrib.auth.models import Group, User
# from .models import User

# Serializers for each models

class BorrowingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowingRecord  # Specifies the model associated with the serializer
        fields = '__all__'       # Includes all fields from the model in the serializer   
        read_only_fields = ["borrowed_date", "status", "due_date"]  # These fields cannot be modified by the users.

    def create(self, validated_data):   # Created custom create method to handle BorrowingRecord creation
        user = self.context["request"].user     # Get the authenticated user from the request context
        member = Member.objects.get(membership_id=user)   # Ensure member = Authenticated / Retrieve the member associated with the authenticated user
        validated_data["member"] = member   # Assign the member to the borrowing record

        # Set the due date to 30 days from the current date
        validated_data['due_date'] = datetime.now() + timedelta(days=30)

        # Call the parent class's create method to save the validated date to the datebase
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
                "write_only": True  # Ensures that the password is write-only and not returned in API responses
            },
            "email": {
                "required": True    # Makes the email field required
            },
            "username": {
                "required": True    # Makes the username field required
            }
        }
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member  
        fields = ["full_name", "email", "phone", "address"]
        read_only_fields = ["membership_id"] # Can't change membership_id(user) when editing.

    def create(self, validated_data):
        user = self.context["request"].user # Get the authenticated user from the request context
        validated_data["membership_id"] = user # Assign the authenticated user as the membership_id 
        return super().create(validated_data)   # Call the parent class's create method to save the validated date to the datebase

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True  # Ensures the password is write-only and not returned in APU responses
            }
        }


