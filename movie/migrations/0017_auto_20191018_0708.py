# Generated by Django 2.2.6 on 2019-10-18 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_auto_20191017_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='trailers',
        ),
        migrations.AddField(
            model_name='movie',
            name='trailers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Trailer'),
        ),
    ]
