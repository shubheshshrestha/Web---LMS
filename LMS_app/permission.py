from .models import Member
from rest_framework.permissions import BasePermission


class IsMember(BasePermission):  # To allow only members to borrow books (Custom permission class)
    # Overwriting method (has_permission)
    def has_permission(self, request, view):  # ,obj for oject-level permissions
        if request.user.is_authenticated:  # Member or not
            return Member.objects.filter(membership_id=request.user).exists() # If user exists in the Member model or not
        return False
        # If user is not authenticated, deny access







# Checks emails and give access accordingly
# class IsExampleDomainUser(BasePermission):
#     """
#     Custom permission to allow only users with '@example.com' emails.
#     """

#     def has_permission(self, request, view):
#         return request.user and request.user.is_authenticated and request.user.email.endswith("@example.com")