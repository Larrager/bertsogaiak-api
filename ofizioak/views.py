from rest_framework import generics

from . import models
from . import serializers

class OfizioaList(generics.ListAPIView):
    queryset = models.Ofizioa.objects.all()
    serializer_class = serializers.OfizioaSerializer


class OfizioaDetail(generics.RetrieveAPIView):
    queryset = models.Ofizioa.objects.all()
    serializer_class = serializers.OfizioaSerializer