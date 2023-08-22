# from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
class ListTodo(generics.ListCreateAPIView):
    # ListCreateAPIView is a generic view that provides GET (list all) and POST method handlers.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo (generics.RetrieveAPIView):  # input parameter ?
    # RetrieveAPIView is used for read-only endpoints to represent a single model instance. 
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
