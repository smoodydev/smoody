# Generated by Django 3.2.5 on 2021-07-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210709_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='recommended',
            field=models.BooleanField(default=True),
        ),
    ]