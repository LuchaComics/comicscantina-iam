# -*- coding: utf-8 -*-
import django_filters
from django_filters import rest_framework as filters
from django.conf.urls import url, include
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics
from rest_framework import authentication, viewsets, permissions, status
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from foundation.models.shared_user import SharedUser
from api.serializers.shared_user import SharedUserListCreateSerializer, SharedUserRetrieveUpdateDestroySerializer


class SharedUserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SharedUserListCreateSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    def get_queryset(self):
        """
        Overriding the initial queryset
        """
        queryset = SharedUser.objects.all()

        # Set up eager loading to avoid N+1 selects
        s = self.get_serializer_class()
        queryset = s.setup_eager_loading(self, queryset)
        return queryset

    def post(self, request, format=None):
        """
        Create
        """
        serializer = SharedUserListCreateSerializer(data=request.data, context={
            # 'created_by': request.user
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class SharedUserCreateValidationAPIView(generics.CreateAPIView):
    """
    API endpoint strictly used for POST creation validations of the
    `SharedUser` model before an actual POST create API call is made.
    """
    serializer_class = SharedUserListCreateSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    def post(self, request, format=None):
        """
        Create
        """
        serializer = SharedUserListCreateSerializer(data=request.data, context={
            # 'created_by': request.user,
        })
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class SharedUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SharedUserRetrieveUpdateDestroySerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    def get(self, request, pk=None):
        """
        Retrieve
        """
        user = get_object_or_404(SharedUser, pk=pk)
        self.check_object_permissions(request, user)  # Validate permissions.
        serializer = SharedUserRetrieveUpdateDestroySerializer(user, many=False)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk=None):
        """
        Update
        """
        self.check_object_permissions(request, user)  # Validate permissions.
        serializer = SharedUserRetrieveUpdateDestroySerializer(user, data=request.data, context={})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        """
        Delete
        """
        user = get_object_or_404(SharedUser, pk=pk)
        self.check_object_permissions(request, user)  # Validate permissions.
        user.delete()
        return Response(data=[], status=status.HTTP_200_OK)
