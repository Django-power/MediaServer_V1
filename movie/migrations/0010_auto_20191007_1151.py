# Generated by Django 2.2.6 on 2019-10-07 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20191007_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[(0, 'Male'), (1, 'Female')], default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='actor',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='movie',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='qualitie',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='key',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='site',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='trailer_type',
            field=models.CharField(max_length=100),
        ),
    ]
