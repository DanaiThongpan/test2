# Generated by Django 4.2.5 on 2023-12-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idc', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
