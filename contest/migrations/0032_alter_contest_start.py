# Generated by Django 4.0.5 on 2022-07-12 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0031_contest_available_contest_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
