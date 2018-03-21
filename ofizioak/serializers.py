from rest_framework import serializers
from . import models

class OfizioaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'metric', 'text', 'created_at', 'updated_at')
        model = models.Ofizioa