# Generated by Django 2.1 on 2020-04-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MRN_number', models.CharField(max_length=264)),
                ('first_name', models.CharField(max_length=264)),
                ('last_name', models.CharField(max_length=264)),
                ('first_symx', models.CharField(max_length=264)),
                ('second_symx', models.CharField(max_length=264)),
                ('third_symx', models.CharField(max_length=264)),
                ('fourth_symx', models.CharField(max_length=264)),
                ('fifth_symx', models.CharField(max_length=264)),
            ],
        ),
    ]
