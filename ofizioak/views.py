from rest_framework import generics, filters
from django_filters import rest_framework as filters2

from . import models
from . import serializers

class OfizioaList(generics.ListAPIView):
    queryset = models.Ofizioa.objects.all()
    serializer_class = serializers.OfizioaSerializer
    filter_backends = (filters.SearchFilter, filters2.DjangoFilterBackend)
    filter_fields = ('metric',)
    search_fields = ('text',)


class OfizioaDetail(generics.RetrieveAPIView):
    queryset = models.Ofizioa.objects.all()
    serializer_class = serializers.OfizioaSerializer