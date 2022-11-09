# Generated by Django 3.2 on 2022-11-07 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.CharField(max_length=50)),
                ('asset_name', models.CharField(max_length=50)),
                ('asset_stat', models.CharField(max_length=50)),
                ('segment_id', models.IntegerField(default=1)),
                ('route_id', models.IntegerField(default=2)),
                ('route_name', models.CharField(default=4, max_length=50)),
                ('route_class', models.CharField(default=1, max_length=50)),
                ('county_id', models.CharField(default='secondary', max_length=50)),
                ('division_id', models.IntegerField(default=4)),
            ],
        ),
    ]
