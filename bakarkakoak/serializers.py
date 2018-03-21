from rest_framework import serializers
from . import models

class BakarkakoaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'type', 'text', 'created_at', 'updated_at')
        model = models.Bakarkakoa