from django.shortcuts import render
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
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
# from rest_framework_simplejwt.tokens import RefreshToken

class BookView(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookTypeView(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializer

class BorrowingRecordView(ModelViewSet):
    permission_classes = []
    queryset = BorrowingRecord.objects.all()
    serializer_class = BorrowingRecordSerializer

class MemberView(ModelViewSet):
    permission_classes = []
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class RegisterView(GenericViewSet):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self,request):
        password = request.data.get("password")
        hash_password = make_password(password)
        data = request.data.copy()
        data["password"] = hash_password
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

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
        
class LoginView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = []

    def create(self,request):
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username,password=password)

            if user == None:
                return Response({"detail":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                token,_ = Token.objects.get_or_create(user=user)
                return Response({"token":token.key},status=status.HTTP_200_OK)

class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = UserSerializer
    

