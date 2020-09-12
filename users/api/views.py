from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin

from .models import User, ProducerProfile
from .serializers import UserSerializer, ProducerProfileSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class ProducerProfileViewSet(ModelViewSet, CreateModelMixin):
    queryset = ProducerProfile.objects.all()
    serializer_class = ProducerProfileSerializer
    permission_classes = (AllowAny,)
        

class UserListView(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Respone(serializer.data)

    def post(self, request, format=None):
        serilazer = UserSerializer(data=request.data)
        if serilazer.is_valid():
            serilazer.save()
            return Response(serilazer.data, status=staus.HTTP_201_CREATED)
        return Response(serilazer.errors, status=status.HTTP_400_BAD_REQUEST)
