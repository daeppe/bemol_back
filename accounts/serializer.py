from rest_framework import serializers
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = [
                'id',
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'complement',
                'number_house',
                'references'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)


class GetIdAccountsSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = [
                'id',
                'username',
                'first_name',
                'last_name',
                'email',
                'complement',
                'number_house',
                'references'
        ]
