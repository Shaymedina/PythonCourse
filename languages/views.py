from django.shortcuts import render
from .models import Language
from .serializers import LanguageSerializer
from rest_framework import viewsets, permissions

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )