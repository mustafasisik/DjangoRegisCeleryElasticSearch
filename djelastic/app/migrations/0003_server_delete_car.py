# Generated by Django 4.2 on 2024-03-18 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_car_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
