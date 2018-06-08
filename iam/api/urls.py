# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import serializers, viewsets, routers
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.shared_user import SharedUserListCreateAPIView, SharedUserCreateValidationAPIView, SharedUserRetrieveUpdateDestroyAPIView


urlpatterns = [
    url(r'^api/users/$', SharedUserListCreateAPIView.as_view(), name='cc_iam_list_create_api_endpoint'),
    url(r'^api/users/validate$', SharedUserCreateValidationAPIView.as_view(), name='cc_iam_pre_create_validation_api_endpoint'),
    url(r'^api/user/(?P<pk>[^/.]+)/$', SharedUserRetrieveUpdateDestroyAPIView.as_view(), name='cc_iam_retrieve_update_destroy_api_endpoint'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
