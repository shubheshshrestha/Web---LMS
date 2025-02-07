from .models import Member
from rest_framework.permissions import BasePermission


class IsMember(BasePermission):  # To allow only members to borrow books

    def has_permission(self, request, view):
        if request.user.is_authenticated:  # Member or not
            return Member.objects.filter(membership_id=request.user).exists()
        return False
       