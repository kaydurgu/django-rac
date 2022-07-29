# Generated by Django 4.0.5 on 2022-07-06 12:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_alter_question_answered_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='contest.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='contest.contest'),
        ),
    ]
