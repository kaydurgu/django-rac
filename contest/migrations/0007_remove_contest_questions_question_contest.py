# Generated by Django 4.0.5 on 2022-07-06 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0006_remove_question_choices_choice_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='contest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contest.contest'),
            preserve_default=False,
        ),
    ]
