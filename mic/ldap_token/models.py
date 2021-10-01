from django.db import models
from datetime import datetime
from datetime import timedelta

# Create your models here.
class AD_token(models.Model):
    username = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    expired_at = models.DateTimeField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.username, self.token)