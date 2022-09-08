from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from accounts.models import User, Profile
from .serializers import UserLoginSerializer, UserSerializer, ProfileSerializer


@api_view(["POST", ])
@permission_classes([AllowAny, ])
def create_user_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        print(password)
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            user = User.objects.create_user(email=email, password=password)
            # user.set_password(password)
            # user.save()
    else:
        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
    return Response(
        {
            "message": "Account created",
            "email": user.email,
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["POST", ])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user.save()

        return Response(
            {
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
            },
            status=status.HTTP_200_OK
        )
    else:
        try:
            message = serializer.errors['non_field_errors'][0]
        except (IndexError, KeyError) as e:
            message = "Some random message I don't know y"

    return Response({'message': message}, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):

    permission_classes(IsAuthenticated)

    def post(self, request):
        print(request.data.dict())
        try:
            profile = Profile.objects.get(user=request.user)
            profile.delete()
        except ObjectDoesNotExist:
            pass
        profile = Profile(user=request.user, **request.data.dict())
        profile.save()
        return Response({"message": "Profile Updated"}, status=status.HTTP_200_OK)

    def get(self, request):
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except ObjectDoesNotExist:
            return Response({"message": "user profile doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
