from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'

class IsSolutionProvider(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'solution_provider'

class IsSolutionSeeker(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'solution_seeker'
