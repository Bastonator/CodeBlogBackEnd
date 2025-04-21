from .models import Category, Snippet, Material
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class SnippetSerializer(ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'