# Generated by Django 4.0.2 on 2022-06-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=70)),
                ('MiddelName', models.CharField(max_length=70)),
                ('LastName', models.CharField(max_length=70)),
                ('Password', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=70)),
                ('Phone', models.IntegerField()),
                ('Address', models.CharField(max_length=100)),
            ],
        ),
    ]
