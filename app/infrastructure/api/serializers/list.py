from rest_framework import serializers
from .item import ItemSerializer


class ListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    items = ItemSerializer(many=True)
