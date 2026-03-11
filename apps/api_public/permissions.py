from rest_framework.permissions import BasePermission


class HasApiKeyPermission(BasePermission):
    message = "API key authentication is not enabled yet."

    def has_permission(self, request, view) -> bool:
        # Placeholder permission class for the first scaffold commit.
        return True
