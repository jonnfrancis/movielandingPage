# Generated by Django 3.2.3 on 2021-08-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_movie_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='clasId',
            field=models.CharField(default='a', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='cool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='kindaCool',
            field=models.BooleanField(default=False),
        ),
    ]
