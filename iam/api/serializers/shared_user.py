# -*- coding: utf-8 -*-
import logging
# import django_rq
# from datetime import datetime, timedelta
# from dateutil import tz
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.db.models import Q, Prefetch
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.http import urlquote
from rest_framework import exceptions, serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from foundation.models.shared_user import SharedUser


logger = logging.getLogger(__name__)


class SharedUserListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SharedUser
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'is_active',
            'is_staff',
            'avatar',
            'last_modified',
            'salt',
            'was_email_activated',
            'pr_access_code',
            'pr_expiry_date'
        )

    def setup_eager_loading(cls, queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related()
        return queryset

    def create(self, validated_data):
        """
        Override the `create` function to add extra functinality.
        """
        #-----------------------------
        # Get our inputs.
        #-----------------------------
        alternate_name = validated_data.get('email', None)

        return validated_data




class SharedUserRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = SharedUser
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'is_active',
            'is_staff',
            'avatar',
            'last_modified',
            'salt',
            'was_email_activated',
            'pr_access_code',
            'pr_expiry_date'
        )

    def setup_eager_loading(cls, queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related()
        return queryset

    def create(self, validated_data):
        """
        Override the `create` function to add extra functinality.
        """
        #-----------------------------
        # Get our inputs.
        #-----------------------------
        alternate_name = validated_data.get('email', None)

        return validated_data
