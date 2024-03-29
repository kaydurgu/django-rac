# Generated by Django 4.0.5 on 2022-07-11 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_profile_followers_alter_profile_followings'),
        ('contest', '0019_remove_contest_result_result_contest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='contest',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='contest.contest'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='result',
            name='participant',
        ),
        migrations.AddField(
            model_name='result',
            name='participant',
            field=models.ManyToManyField(blank=True, to='members.profile'),
        ),
    ]
