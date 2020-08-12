from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class HelloApiView(APIView):
    '''Test API View'''
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns A list of APIView features"""
        an_apiview = [
            'Uses Http methods as f(get, put, post, patch and delete)',
            'Similar to a Django CBV',
            'Gives more control',
            'Mapped Manually',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create Hello Message With POST"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Thank You for messaging, {name}.'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        """Handle Update An Object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partial Update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle Deletetion Of An Object"""
        return Response({'method': 'DELETE'})
