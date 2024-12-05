from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

# Create your views here.

class CategoryList(APIView):
    serializer_class = CategorySerializer

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(
            categories, many=True, context={"request": request}
        )
        return Response(serializer.data)