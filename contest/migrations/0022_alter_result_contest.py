# Generated by Django 4.0.5 on 2022-07-11 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0021_remove_result_participant_result_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.contest'),
        ),
    ]