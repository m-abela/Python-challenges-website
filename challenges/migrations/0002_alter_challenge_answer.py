# Generated by Django 4.2.5 on 2023-09-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='answer',
            field=models.CharField(max_length=100),
        ),
    ]
