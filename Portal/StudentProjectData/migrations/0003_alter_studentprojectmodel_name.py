# Generated by Django 3.2.8 on 2021-12-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProjectData', '0002_auto_20211206_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprojectmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
