# Generated by Django 2.0.4 on 2018-06-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_guests', '0006_auto_20180612_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order_no',
            field=models.IntegerField(default=None, verbose_name='Nr porządkowy'),
            preserve_default=False,
        ),
    ]