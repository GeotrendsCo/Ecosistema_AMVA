# Generated by Django 4.2.6 on 2023-10-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userAttributes',
            fields=[
                ('username', models.CharField(max_length=400, primary_key=True, serialize=False, verbose_name='username')),
                ('usercode', models.CharField(max_length=7, verbose_name='usercode')),
                ('first_name', models.CharField(max_length=400, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=400, verbose_name='last_name')),
                ('email', models.CharField(max_length=400, verbose_name='email')),
                ('country', models.CharField(max_length=400, verbose_name='country')),
                ('city', models.CharField(max_length=400, verbose_name='city')),
                ('entity', models.CharField(max_length=400, verbose_name='entity')),
            ],
        ),
    ]
