from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

from rest_framework import serializers

from accounts.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'date_joined', 'last_login']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'email': {
                'required': True
            },
            'password': {
                'write_only': True,
                'required': True
            },
            'date_joined': {
                'read_only': True
            },
            'last_login': {
                'read_only': True
            },

        }


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'email': {
                'required': True
            }
        }


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("password", ),
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = _("Unable to Login with the credentials provided")
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _("Must include email and password.")
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.EmailField(label=_("Email"))

    class Meta:
        model = Profile
        fields = ['user', 'full_name', 'contact', 'college_name', 'year_of_study']
        extra_kwargs = {
            "user": {
                "required": True
            }
        }
