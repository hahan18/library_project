from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema

from .filters import BookFilter
from .models import Book
from .serializers import BookSerializer


@extend_schema(
    summary="Manage Books",
    description=(
            "This viewset allows you to perform CRUD operations on the Book model. "
            "You can create, retrieve, update, or delete books. Additionally, you can filter books by author, "
            "published_date, and language. Use the `page_size` query parameter to control pagination."
    ),
    responses={
        200: BookSerializer(many=True),
        201: BookSerializer,
        400: "Bad Request",
        404: "Not Found",
    },
    tags=["Books"]
)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
