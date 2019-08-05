from django.urls import path, include
from mackta_api.api.views import UserProfileViewSet, TrainDataAPIView # UserProfileFeedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('user-viewset', views.UserViewSet, base_name='user-viewset')
router.register(r"profiles", UserProfileViewSet)
router.register(r"tansportation_list", TrainDataAPIView, basename='traindata')
# router.register(r"feed", UserProfileFeedViewSet )
# router.register(r"detail", CustomRegistrationView, basename='detail')

urlpatterns = [
    path('', include(router.urls)),
    # path('user-view/', views.UserAPIView.as_view()),
    # path('login/', views.UserLoginAPIView.as_view()),
]