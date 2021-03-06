# Generated by Django 3.2.9 on 2021-11-19 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EKScooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ek_scooters', to='area.area')),
            ],
            options={
                'db_table': 'ek_scooter',
            },
        ),
        migrations.CreateModel(
            name='BoardingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_end_lat', models.DecimalField(decimal_places=14, max_digits=17)),
                ('use_end_lng', models.DecimalField(decimal_places=14, max_digits=17)),
                ('use_start_at', models.DateTimeField()),
                ('use_end_at', models.DateTimeField()),
                ('in_use', models.BooleanField()),
                ('fee', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ek_scooter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boarding_logs', to='vehicle.ekscooter')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boarding_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'boarding_log',
            },
        ),
    ]
