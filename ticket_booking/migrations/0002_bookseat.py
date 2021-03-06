# Generated by Django 3.1.4 on 2022-05-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('userEmail', models.CharField(default='', max_length=50)),
                ('whereTo', models.CharField(default='', max_length=50)),
                ('howMany', models.CharField(default='', max_length=50)),
                ('arrivals', models.CharField(default='', max_length=50)),
                ('leaving', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
