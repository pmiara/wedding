# Generated by Django 2.0.4 on 2018-06-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_guests', '0005_auto_20180609_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nazwa')),
                ('header', models.CharField(max_length=100, verbose_name='Nagłówek')),
                ('content', models.TextField(verbose_name='Treść')),
                ('image', models.ImageField(upload_to='', verbose_name='Zdjęcie')),
            ],
        ),
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(editable=False, max_length=30, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='surname',
            field=models.CharField(editable=False, max_length=50, verbose_name='Nazwisko'),
        ),
    ]
