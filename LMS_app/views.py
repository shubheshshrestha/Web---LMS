# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Book, BookType, BorrowingRecord, Member
from .serializer import BookSerializer, UserSerializer, BookTypeSerializer, BorrowingRecordSerializer, MemberSerializer, LoginSerializer
from django.contrib.auth.models import Group, User
# from .models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
# from rest_framework_simplejwt.tokens import RefreshToken
from .permission import IsMember
from django_filters.rest_framework import DjangoFilterBackend

#ViewSet for managing Book objects
class BookView(ModelViewSet):
    permission_classes = []     # No specific permissions required to access this view
    queryset = Book.objects.all()      # Retrieve all Book objects from the database
    serializer_class = BookSerializer      # BookSerializer used to serialize or deserialize data
    filter_backends = [DjangoFilterBackend]        # Enable filtering using DjangoFilterBackend
    filterset_fields = ['title', 'author', 'isbn', 'description', 'category']    # Didn't include other remaining variables because it's not necessary for the user
    search_fields = ['title', 'author', 'isbn', 'description', 'category']    # Fields available for filtering and searching

class BookTypeView(ModelViewSet):
    permission_classes = []
    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['name']

class BorrowingRecordView(ModelViewSet):
    permission_classes = [IsMember]  # Only Members can access this view.
    queryset = BorrowingRecord.objects.all()
    serializer_class = BorrowingRecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'member',  'borrowed_date', 'due_date']
    search_fields = ['book', 'member', 'borrowed_date', 'due_date']

class MemberView(ModelViewSet):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    queryset = Member.objects.all() 
    serializer_class = MemberSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['full_name', 'email', 'phone', 'membership_id']
    search_fields = ['full_name', 'email', 'phone', 'membership_id']

class RegisterView(GenericViewSet):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Creates or Registers a new user
    def create(self,request):
        password = request.data.get("password")     # Get the password from the request data
        hash_password = make_password(password)     # For secure storage
        data = request.data.copy()                  # Create a copy of the request data to avoid modifying the original
        data["password"] = hash_password            # Replace the plain password with the hashed password
        serializer = UserSerializer(data=data)      # Validate and serialize the data

        if serializer.is_valid():   # Save the user if data is valid
            serializer.save()       # Save the new user in the database
            return Response(serializer.data)    # Return the serialized user data
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Else, return errors if the data is invalid
        

# class LoginView(GenericViewSet):
#     def create(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')

        # # Authenticate the user
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     refresh = RefreshToken.for_user(user)
        #     return Response({
        #         "refresh": str(refresh),
        #         "access": str(refresh.access_token),
        #     }, status=status.HTTP_200_OK)
        # else:
        #     return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericViewSet):  # ViewSet for handling user login functionality
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [] # Open to all

    # Handles user login by validating credentials and returning an authentication token
    def create(self,request):
            username = request.data.get("username") # Get the username from the request data
            password = request.data.get("password") # Get the password from the request data
            user = authenticate(username=username,password=password) # Authenticate the User

            if user == None:
                return Response({"detail":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)  # If authentication fails, return an error response
            else:   
                token,_ = Token.objects.get_or_create(user=user) # If authentication succeeds, generate or retrieve a token for the user
                return Response({"token":token.key},status=status.HTTP_200_OK)  # Return the token in the response

class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = UserSerializer
    

