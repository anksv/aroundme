# Generated by Django 2.1.3 on 2018-12-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.IntegerField()),
                ('lshortname', models.CharField(max_length=3)),
                ('lname', models.CharField(max_length=50)),
            ],
        ),
    ]
