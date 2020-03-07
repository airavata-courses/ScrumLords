from django.contrib import admin

# Register your models here.
from api_manager.models.city import City
from api_manager.models.session import Session

admin.site.register(Session)
admin.site.register(City)
