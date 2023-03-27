from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from acc.models import User
from acc.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
