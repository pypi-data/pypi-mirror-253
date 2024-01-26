from django.db import models

from . import Company
from .sector import Sector
from .country import Country
from .base import BaseModelAbstract
from .user import User


class CompanyConfiguration(BaseModelAbstract, models.Model):
    created_by = None
    company = models.OneToOneField(Company, models.CASCADE,
                                   related_name='config')
    countries = models.ManyToManyField(Country, null=True, blank=True)
    sectors = models.ManyToManyField(Sector, null=True, blank=True)
    maturity = models.IntegerField(default=0)
    discount_range = models.JSONField(default=list([1, 50]))

    def __unicode__(self):
        return f"{self.company}'s config"
