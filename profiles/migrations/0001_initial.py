# Generated by Django 4.0 on 2022-01-10 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=5)),
                ('tnr', models.CharField(max_length=5)),
                ('age', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
