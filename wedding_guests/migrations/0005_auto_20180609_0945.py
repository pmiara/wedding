# Generated by Django 2.0.4 on 2018-06-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_guests', '0004_auto_20180516_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='gift',
            field=models.CharField(blank=True, max_length=50, verbose_name='Prezent'),
        ),
    ]
