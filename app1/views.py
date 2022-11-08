from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

class BasicAuthView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {
            'Data': "Validation succesfull for Basic Authentication",
            'user': str(request.user),
        }
        return Response(content)

class TokenExampleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {
            'Data': "Validation succesfull for Token Authentication",
            'user': str(request.user),
        }
        return Response(content)

class JwtExampleView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {
            'Data': "Validation succesfull for JWT token.",
            'user': str(request.user),
        }
        return Response(content)
