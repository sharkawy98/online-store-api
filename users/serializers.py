from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = User
        fields = [
            'id' , 
            'username', 
            'password', 
            'is_superuser', 
            'is_store_owner',
	        'date_joined',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
	        'date_joined': {'read_only': True},
            'is_store_owner': {'required': True},
        }


    def create(self, validated_data):
        user = User(username=validated_data['username'],)
        user.set_password(validated_data['password'])
        
        if validated_data['is_store_owner']:
            user.is_store_owner = True
        # admin will added after login service
        
        user.save()
        return user