from django.urls import path, include
from mackta_api.api.views import UserProfileViewSet # UserProfileFeedViewSet
from rest_framework.routers import DefaultRouter
from mackta_api.api.views import CurrentUserAPIView

router = DefaultRouter()
# router.register('user-viewset', views.UserViewSet, base_name='user-viewset')
router.register(r"profiles", UserProfileViewSet)
# router.register(r"feed", UserProfileFeedViewSet )
# router.register(r"detail", CustomRegistrationView, basename='detail')

urlpatterns = [
    path('', include(router.urls)),
    path("user/", CurrentUserAPIView.as_view(), name="current-user")
    # path('user-view/', views.UserAPIView.as_view()),
    # path('login/', views.UserLoginAPIView.as_view()),
]