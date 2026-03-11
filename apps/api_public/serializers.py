from rest_framework import serializers


class ApiRootSerializer(serializers.Serializer):
    name = serializers.CharField()
    version = serializers.CharField()
    docs = serializers.CharField()
