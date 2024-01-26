from django.db import models

from .base import BaseModelAbstract


class BaseRate(BaseModelAbstract, models.Model):
    rate = models.FloatField(help_text="Rate in percentage")
    duration = models.IntegerField(help_text='Maturity in months')
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return f"{self.date} - {self.rate} - {self.duration}"
