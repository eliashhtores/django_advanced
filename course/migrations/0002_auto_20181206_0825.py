# Generated by Django 2.0.2 on 2018-12-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='credits',
            field=models.IntegerField(),
        ),
    ]
