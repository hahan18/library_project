from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    @staticmethod
    def validate_isbn(value):
        if len(value) != 13 or not value.isdigit():
            raise serializers.ValidationError("ISBN must be exactly 13 digits.")
        return value
