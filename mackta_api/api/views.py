from rest_framework.views import APIView
from rest_framework import status, viewsets, mixins, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.settings import api_settings
# from rest_framework.response import Response

from mackta_api.api.serializers import CustomRegisterSerializer #CustomUserDetailsSerializer
from mackta_api.models import User #, ProfileFeedItem
# from mackta_api.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly
from rest_auth.registration.views import RegisterView


class UserProfileViewSet(mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """handling creating and updating profiles"""
    serializer_class = CustomRegisterSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

# class UserProfileFeedViewSet(mixins.UpdateModelMixin,
#                         mixins.ListModelMixin,
#                         mixins.RetrieveModelMixin,
#                         viewsets.GenericViewSet):
#     """Handles creating, reading and updating profile feed items"""
#     serializer_class = ProfileFeedItemSerializer
#     queryset = ProfileFeedItem.objects.all()

#     def perform_create(self, serializer):
#         """Sets the user profile to the logged in user"""
#         serializer.save(user_profile=self.request.user)
    
# class CustomRegistrationView(RegisterView):
#     serializer_class = CustomUserDetailsSerializer

class CurrentUserAPIView(APIView) :
    def get(self, request) :
        serializer = CustomRegisterSerializer(request.user)
        return Response(serializer.data)