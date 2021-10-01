from django.conf import settings
from django.db import models

class CompanyMonthsLimit(models.Model):
    company = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    months = models.IntegerField()
    def __str__(self):
        return self.company.username
