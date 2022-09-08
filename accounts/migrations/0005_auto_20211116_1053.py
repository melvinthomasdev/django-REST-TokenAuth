# Generated by Django 3.2.9 on 2021-11-16 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211116_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='college_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='year_of_study',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=65)),
                ('contact', models.CharField(max_length=13)),
                ('college_name', models.CharField(max_length=150)),
                ('year_of_study', models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]