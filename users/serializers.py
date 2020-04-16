from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# to display the value of the user type key in JSON Response
# (ex: 'normal' --> 'user_type': 'Normal user')
class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]


class UserSerializer(serializers.ModelSerializer):
    user_type = ChoiceField(choices=User.USER_TYPES)

    class Meta:
        model = User
        fields = [
            'id' , 
            'username', 
            'password', 
            'user_type',
	        'date_joined',     
        ]
        extra_kwargs = {
            'password': {'write_only': True},
	        'date_joined': {'read_only': True, 'format': "%d-%m-%Y %H:%M:%S"},
        }


    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            user_type = validated_data['user_type'],)
        user.set_password(validated_data['password'])

        type = validated_data['user_type']
        if type == 'owner':
            user.is_staff = True
        elif type == 'admin':
            user.is_staff = True
            user.is_superuser = True
        
        user.save()
        return user