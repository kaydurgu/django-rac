# Generated by Django 4.0.5 on 2022-07-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images/profile/'),
        ),
    ]
