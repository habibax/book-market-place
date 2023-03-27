from rest_framework_simplejwt.views import TokenObtainPairView
from acc.serializers import TokenObtainPairSerializer
class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


