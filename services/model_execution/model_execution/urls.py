"""model_execution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from ml_model.views.forecast import forecast_weather
from ml_model.views.health_check import health_check, ready_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dark/forecast", forecast_weather),
    url(r"^ht", health_check),
    url(r"^", ready_check),
]
