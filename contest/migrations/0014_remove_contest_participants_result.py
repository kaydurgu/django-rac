# Generated by Django 4.0.5 on 2022-07-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_profile_followers_alter_profile_followings'),
        ('contest', '0013_remove_contest_results_delete_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='participants',
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('participant', models.ManyToManyField(blank=True, to='members.profile')),
            ],
        ),
    ]
