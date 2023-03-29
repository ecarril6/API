from rest_framework import serializers
from api.models import preProcessedImages, newTable

class preProcessedImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = preProcessedImages
        fields = ('__all__')


class newTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = newTable
        fields = ('__all__')
