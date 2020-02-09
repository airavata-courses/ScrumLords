import uuid

from django.db import models

from model_utils.models import SoftDeletableModel, TimeStampedModel


class Session(TimeStampedModel, SoftDeletableModel):
    visible_id = models.UUIDField(default=uuid.uuid4, editable=False, null=False)
    geo_id = models.IntegerField(null=False)
    name = models.CharField(max_length=200, null=False)
    alternate_names = models.CharField(max_length=5000, null=True)
    latitude = models.CharField(max_length=50, null=False)
    longitude = models.CharField(max_length=50, null=False)
    country_code = models.CharField(max_length=35, null=True)
    admin_code = models.CharField(max_length=100, null=True)
    population = models.IntegerField(null=False)
    elevation = models.CharField(max_length=100, null=True)
    timezone = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=30, null=False)
    user_id = models.IntegerField(null=False)

    class Meta:
        db_table = "sessions"
