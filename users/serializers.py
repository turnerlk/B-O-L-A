from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

    def validate(self, attrs):
        name = attrs.get('name')
        email = attrs.get('email')
        password = attrs.get('password')

        errors = {}

        if not name:
            errors['name'] = 'Please provide an username.'

        if not email:
            errors['email'] = 'Please provide an email.'

        if not password:
            errors['password'] = 'Please provide an password.'

        if errors:
            raise ValidationError({'message': errors})

        return attrs