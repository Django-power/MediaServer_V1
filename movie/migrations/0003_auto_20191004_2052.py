# Generated by Django 2.2.6 on 2019-10-04 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20191004_2049'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actor',
            new_name='Actors',
        ),
        migrations.RenameModel(
            old_name='Collection',
            new_name='Collections',
        ),
        migrations.RenameModel(
            old_name='Genre',
            new_name='Genres',
        ),
        migrations.RenameModel(
            old_name='Movie',
            new_name='Movies',
        ),
        migrations.RenameModel(
            old_name='Qualitie',
            new_name='Qualities',
        ),
        migrations.RenameModel(
            old_name='Trailer',
            new_name='Trailers',
        ),
        migrations.RenameModel(
            old_name='Year',
            new_name='Years',
        ),
    ]