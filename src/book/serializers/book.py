from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'cover_image', 'price']

class BookCreateSerializer(serializers.ModelSerializer):
    cover_image = serializers.ImageField()

    class Meta:
        model = Book
        fields = ['title', 'description', 'cover_image', 'price']