# Generated by Django 4.0.5 on 2022-07-11 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_profile_followers_alter_profile_followings'),
        ('contest', '0015_result_contest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='participant',
        ),
        migrations.AddField(
            model_name='result',
            name='participant',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='members.profile'),
            preserve_default=False,
        ),
    ]
