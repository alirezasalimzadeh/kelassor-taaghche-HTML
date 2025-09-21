from rest_framework import generics, filters
from book.models import Category, AudioBook, PrintedBook
from book.serializer import CategorySerializer, PrintedBookSerializer, AudioBookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyUpdateRetrieve(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class AudioBookListCreate(generics.ListCreateAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'category']
    search_fields = ['name', 'author']
    ordering_fields = ['name']


class PrintedBookListCreate(generics.ListCreateAPIView):
    queryset = PrintedBook.objects.all()
    serializer_class = PrintedBookSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'category']
    search_fields = ['name', 'author']
    ordering_fields = ['name']


class AudioBookDestroyUpdateRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer



class PrintedBookDestroyUpdateRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrintedBook.objects.all()
    serializer_class = PrintedBookSerializer
