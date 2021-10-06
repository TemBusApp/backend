from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

from rest_framework import serializers


from rest_framework_jwt.settings import api_settings

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(User.objects.all())]
    )
    password = serializers.CharField(
        validators=[validate_password],
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'phone',
            'username', 'email', 'password'
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if 'password' in rep:
            del rep['password']
        #retorna o token de acesso do usuario cadastrado

        payload = api_settings.JWT_PAYLOAD_HANDLER(instance)
        token = api_settings.JWT_ENCODE_HANDLER(payload)
        rep['acess_token'] = token
        return rep

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class ProfileUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    descriptions = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id', 'name', 'descriptions',
        ]

    def get_descriptions(self, obj):
        ds = Description.objects.filter(user=obj)
        serializer = CreateDescriptionSerializer(ds, many=True)
        return serializer.data

    def get_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)