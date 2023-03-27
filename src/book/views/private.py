from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from book.models import Book
from book.serializers import BookSerializer,BookCreateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return Book.objects.filter(author=self.request.user)
    def get_serializer_class(self):
        if self.action == 'create':
            return BookCreateSerializer
        else:
            return BookSerializer
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['author'] = request.user
                book = serializer.save()

                image_file = request.data.get('cover_image')
                if image_file:
                    book.cover_image.save(image_file.name, image_file, save=True)

                return Response({"message":"book published successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except FileNotFoundError as err:
            return Response( status=status.HTTP_201_CREATED)
        
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    @action(detail=True, methods=['delete'])
    def unpublish(self, request, pk=None):
        book = self.get_object()
        if book.author==self.request.user:
            book.published = False
            book.save()
            return Response({'status': 'unpublished'})
        else:
            return Response({'status': 'unauthorized'})
            


    
