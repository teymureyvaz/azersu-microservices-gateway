from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length=255)
    expire_date = serializers.DateTimeField()
    status = serializers.IntegerField()
    message = serializers.CharField(max_length=255)

class ResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField(max_length=50)

class ResponseCheckSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    status = serializers.IntegerField()
    message = serializers.CharField(max_length=50)