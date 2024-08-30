from rest_framework import permissions


class IsUserOrCreatingAccountOrReadOnly(permissions.BasePermission):
    """
    Object-level permission that allows users to create accounts or edit their
    own accounts.
    """

    def has_object_permission(self, request, view, obj):
        user_is_making_new_account = view.action == 'create'
        if user_is_making_new_account:
            return True

        is_read_only_action = request.method in permissions.SAFE_METHODS
        if is_read_only_action:
            return True

        is_accessing_their_own_user_object = obj == request.user
        return is_accessing_their_own_user_object
