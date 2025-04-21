from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .models import Material,Snippet
from .serializers import MaterialSerializer, SnippetSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.db.models import Q


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def materials(request):
    materials = Material.objects.all()
    serializer = MaterialSerializer(materials, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def material(request, slug):
    material = Material.objects.get(slug=slug)
    serializer = MaterialSerializer(material, many=False)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def snippets(request, slug):
    material = get_object_or_404(Material, slug=slug)
    snippets = Snippet.objects.filter(material=material)

    serializer = SnippetSerializer(snippets, many=True)

    return JsonResponse({
        'data': serializer.data
    })