# Generated by Django 3.1.4 on 2021-02-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210226_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
