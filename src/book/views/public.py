from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from book.models import Book
from book.serializers import BookSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.filter(published=True)
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author','description', 'price']

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.filter(published=True)
    serializer_class = BookSerializer
    lookup_field = 'id'
