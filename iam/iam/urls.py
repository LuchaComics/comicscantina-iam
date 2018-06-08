"""comicscantina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView


# Base URLs.
urlpatterns = [
    # # Here are a list of URLs we'd like to have to help users who enter
    # # URLs from memory and or do not know the URLs. These redirects are for
    # # user's convinience.
    # url(r'^login/', RedirectView.as_view(pattern_name='workery_login_master', permanent=True, query_string=True)),
    # url(r'^login', RedirectView.as_view(pattern_name='workery_login_master', permanent=True, query_string=True)),
    # url(r'^sign-in/', RedirectView.as_view(pattern_name='workery_login_master', permanent=True, query_string=True)),
    # url(r'^sign-in', RedirectView.as_view(pattern_name='workery_login_master', permanent=True, query_string=True)),

    # Here are where the applications URL start.
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls), # Our project does not support Django Admin.

    #  # Sitemap
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #
    # # Django-RQ
    # url(r'^django-rq/', include('django_rq.urls')),

    url(r'^', include('api.urls')),
]

# Serving our URLs.
urlpatterns += i18n_patterns(

)
