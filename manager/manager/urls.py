"""manager URL Configuration

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

from api_manager.views.firestore_get import (
    get_retrieved_data,
    get_forecast_data,
    get_processed_data,
)
from api_manager.views.session_create import start_session_pipeline
from api_manager.views.session_get import get_all_sessions, get_session
from api_manager.views.session_status import get_session_status, update_session_status

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"session/create", start_session_pipeline),
    url(r"^session/(?P<session_id>\w+)/status", get_session_status),
    url(r"^session/status", update_session_status),
    url(r"^user/(?P<user_id>\w+)/sessions", get_all_sessions),
    url(r"^session/(?P<session_id>\w+)/get", get_session),
    url(r"^session/(?P<session_id>\w+)/history", get_retrieved_data),
    url(r"^session/(?P<session_id>\w+)/forecast", get_forecast_data),
    url(r"^session/(?P<session_id>\w+)/forecast", get_processed_data),
]
