from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import status

from .models import Profile


def need_profile(view_function):
    def wrapper(request, *args, **kwargs):
        try:
            Profile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response({"message": "You need to complete profile first"}, status=status.HTTP_400_BAD_REQUEST)
        return view_function(request, *args, **kwargs)
    return wrapper
