# Generated by Django 3.1.7 on 2021-03-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0005_auto_20210228_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='curso',
            field=models.CharField(blank=True, max_length=5, verbose_name='curso'),
        ),
    ]
