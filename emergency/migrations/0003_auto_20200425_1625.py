# Generated by Django 2.1.5 on 2020-04-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0002_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='symx',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='symx',
            name='fifth_symx',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='symx',
            name='fourth_symx',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
