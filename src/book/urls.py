from .views import BookListAPIView, BookDetailAPIView,BookViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    path('<int:id>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('user', include(router.urls)),
    
]


