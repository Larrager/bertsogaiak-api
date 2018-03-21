from rest_framework import generics

from . import models
from . import serializers

class BakarkakoaList(generics.ListAPIView):
    queryset = models.Bakarkakoa.objects.all()
    serializer_class = serializers.BakarkakoaSerializer


class BakarkakoaDetail(generics.RetrieveAPIView):
    queryset = models.Bakarkakoa.objects.all()
    serializer_class = serializers.BakarkakoaSerializer
