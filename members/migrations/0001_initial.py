# Generated by Django 4.0.5 on 2022-07-05 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('followers', models.ManyToManyField(related_name='myfollowers', to='members.profile')),
                ('followings', models.ManyToManyField(related_name='myfollowings', to='members.profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
