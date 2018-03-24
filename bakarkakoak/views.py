from rest_framework import generics, filters
from django_filters import rest_framework as filters2

from . import models
from . import serializers

class BakarkakoaList(generics.ListAPIView):
    queryset = models.Bakarkakoa.objects.all()
    serializer_class = serializers.BakarkakoaSerializer
    filter_backends = (filters.SearchFilter, filters2.DjangoFilterBackend)
    filter_fields = ('type',)
    search_fields = ('text',)


class BakarkakoaDetail(generics.RetrieveAPIView):
    queryset = models.Bakarkakoa.objects.all()
    serializer_class = serializers.BakarkakoaSerializer
