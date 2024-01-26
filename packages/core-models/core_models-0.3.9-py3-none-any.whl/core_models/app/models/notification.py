from django.db import models

from . import Company
from .base import BaseModelAbstract


class Notification(BaseModelAbstract, models.Model):
    company = models.ForeignKey(Company, models.CASCADE, null=True, blank=True)
    notice_type = models.CharField(max_length=50, null=False, blank=False)
    object_id = models.UUIDField(null=True, blank=True)
    seen = models.BooleanField(default=False)

    def __unicode__(self):
        email = self.created_by.email if self.created_by else '-'
        return f"Notification type: {self.notice_type} for: {email}"

    @property
    def text(self):
        return ''
