# from rest_framework import permissions

# class IsOwnProfileOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # print(obj, request)
#         return obj.id == request.user.id


# class IsOwnerOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         print(obj, request)
#         return obj.user_profile == request.user.profile