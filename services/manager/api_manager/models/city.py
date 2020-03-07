from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class City(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=200, null=False)
    ascii_name = models.CharField(max_length=200, null=True)
    alternate_names = models.CharField(max_length=5000, null=True)
    latitude = models.CharField(max_length=50, null=False)
    longitude = models.CharField(max_length=50, null=False)
    feature_class = models.CharField(max_length=100, null=True)
    feature_code = models.CharField(max_length=100, null=True)
    country_code = models.CharField(max_length=100, null=True)
    alternate_country_code = models.CharField(max_length=100, null=True)
    admin_code_1 = models.CharField(max_length=100, null=True)
    admin_code_2 = models.CharField(max_length=100, null=True)
    admin_code_3 = models.CharField(max_length=100, null=True)
    admin_code_4 = models.CharField(max_length=100, null=True)
    population = models.IntegerField(null=False)
    elevation = models.CharField(max_length=100, null=True)
    timezone = models.CharField(max_length=100, null=False)
    modification_date = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "cities"
