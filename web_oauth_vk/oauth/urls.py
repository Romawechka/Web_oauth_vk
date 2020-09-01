"""web_oauth_vk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.urls import path, include
from allauth.utils import import_attribute
from .spec.providers.vk.provider import VKProvider
from allauth.account import views as account_views

login_view = import_attribute(VKProvider.get_package() + '.views.oauth2_login')
callback_view = import_attribute(VKProvider.get_package() + '.views.oauth2_callback')



urlpatterns = [
    path('', views.login, name='account_login'),
    path('vk/', login_view, name='vk_login'),
    path('vk/callback/', callback_view, name="vk_callback"),
    path('logout/', account_views.logout, name='account_logout'),
]
