# Generated by Django 2.2.10 on 2020-05-10 07:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20200510_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentar',
            name='komentar',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='komentar',
            name='rating',
            field=models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
