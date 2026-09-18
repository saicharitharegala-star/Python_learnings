from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Allow access only to the user who created the post."""

    message = "You can only access your own blog posts."

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
