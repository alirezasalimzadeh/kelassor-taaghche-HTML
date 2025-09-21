from rest_framework import serializers
from book.models import Category, PrintedBook, AudioBook


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PrintedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintedBook
        fields = '__all__'


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = '__all__'
