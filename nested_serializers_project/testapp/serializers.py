from django.db.models import fields
from testapp.models import Author,Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        
class AuthorSerializer(serializers.ModelSerializer):
    book_by_author=BookSerializer(read_only=True,many=True)
    class Meta:
        model=Author
        fields='__all__'

