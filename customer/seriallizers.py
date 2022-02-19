from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    
    
class PostSerializer(serializers.Serializer):
    created_on = serializers.DateTimeField()