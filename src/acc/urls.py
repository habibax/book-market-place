from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from acc.views import TokenObtainPairView
from acc.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
