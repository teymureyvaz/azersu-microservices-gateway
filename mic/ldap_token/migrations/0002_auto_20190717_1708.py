# Generated by Django 2.2.3 on 2019-07-17 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldap_token', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_token',
            name='expired_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 18, 17, 7, 59, 932674)),
        ),
    ]
