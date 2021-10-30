# Generated by Django 3.2.3 on 2021-08-01 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='backgroundPhoto',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='directors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='backgroundPhoto',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
