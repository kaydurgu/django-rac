# Generated by Django 4.0.5 on 2022-07-11 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0022_alter_result_contest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='contest',
        ),
        migrations.AddField(
            model_name='contest',
            name='contest',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='contest.result'),
            preserve_default=False,
        ),
    ]
