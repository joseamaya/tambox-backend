import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from rest_framework import status
from authentication.serializers import UserSerializer

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username', None)
        password = data.get('password', None)

        cuenta = authenticate(username=username, password=password)
        if cuenta is not None:
            if cuenta.is_active:
                login(request, cuenta)
                serialized = UserSerializer(cuenta)
                return JsonResponse(serialized.data)
            else:
                return JsonResponse({
                    'status': 'Desautorizado',
                    'message': 'Esta cuenta ha sido deshabilitado',
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({
                'status': 'Desautorizado',
                'message': 'Usuario o Password incorrectos',
            }, status=status.HTTP_401_UNAUTHORIZED)