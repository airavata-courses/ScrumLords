from django.db import models

from model_utils.models import SoftDeletableModel, TimeStampedModel


class Session(TimeStampedModel, SoftDeletableModel):
    geo_id = models.IntegerField(null=False)
    name = models.CharField(max_length=100, null=False)
    alternate_names = models.CharField(max_length=1200, null=True)
    latitude = models.CharField(max_length=25, null=False)
    longitude = models.CharField(max_length=25, null=False)
    country_code = models.CharField(max_length=5, null=False)
    admin_code = models.CharField(max_length=5, null=True)
    population = models.IntegerField(null=False)
    elevation = models.CharField(max_length=15, null=True)
    timezone = models.CharField(max_length=30, null=False)
    status = models.CharField(max_length=15, null=False)
    user_id = models.IntegerField(null=False)

    class Meta:
        db_table = "sessions"
