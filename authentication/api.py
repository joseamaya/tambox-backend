import json
from django.contrib.auth import authenticate, login
from rest_framework import status, views
from rest_framework.response import Response
from authentication.serializers import UserSerializer

class LoginView(views.APIView):

    def post(self, request, format = None):
        data = json.loads(request.body)
        username = data.get('username', None)
        password = data.get('password', None)

        cuenta = authenticate(username=username, password=password)
        if cuenta is not None:
            if cuenta.is_active:
                login(request, cuenta)
                serialized = UserSerializer(cuenta)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Desautorizado',
                    'message': 'Esta cuenta ha sido deshabilitado',
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Desautorizado',
                'message': 'Usuario o Password incorrectos',
            }, status=status.HTTP_401_UNAUTHORIZED)