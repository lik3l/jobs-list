# Generated by Django 2.1.5 on 2019-01-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190120_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='default_price',
            field=models.FloatField(default=10),
        ),
    ]
