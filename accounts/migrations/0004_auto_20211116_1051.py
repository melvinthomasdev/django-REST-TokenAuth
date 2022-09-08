# Generated by Django 3.2.9 on 2021-11-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211116_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='college_name',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(blank=True, default=None, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, default=None, max_length=65, null=True),
        ),
    ]