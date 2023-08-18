# from django.shortcuts import render
from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()    # todo: search basic sql apis
    serializer_class = BookSerializer
