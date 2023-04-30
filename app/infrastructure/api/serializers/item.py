from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
