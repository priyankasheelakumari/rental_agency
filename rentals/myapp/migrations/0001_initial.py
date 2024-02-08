# Generated by Django 4.2.3 on 2023-07-24 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='four_wheeler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agencyno', models.IntegerField(null=True)),
                ('Rcno', models.IntegerField(null=True)),
                ('Vehicleno', models.IntegerField(null=True)),
                ('Type_of_vehicle', models.CharField(max_length=50, null=True)),
                ('No_of_seats', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='heavy_wheeler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agencyno', models.IntegerField(null=True)),
                ('Rcno', models.IntegerField(null=True)),
                ('Vehicleno', models.IntegerField(null=True)),
                ('Type_of_vehicle', models.CharField(max_length=50, null=True)),
                ('No_of_seats', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='two_wheeler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agencyno', models.IntegerField(null=True)),
                ('Rcno', models.IntegerField(null=True)),
                ('Vehicleno', models.IntegerField(null=True)),
                ('Type_of_vehicle', models.CharField(max_length=50, null=True)),
                ('No_of_seats', models.IntegerField(null=True)),
                ('userR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='agency_reg',
            fields=[
                ('Agencyno', models.IntegerField(primary_key=True, serialize=False)),
                ('Uname', models.CharField(max_length=50, null=True)),
                ('Name', models.CharField(max_length=30, null=True)),
                ('Aname', models.CharField(max_length=50, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Place', models.CharField(max_length=50, null=True)),
                ('Licno', models.IntegerField(null=True)),
                ('Mobno', models.IntegerField(null=True)),
                ('Password', models.CharField(max_length=30, null=True)),
                ('approve', models.CharField(default='no', max_length=30, null=True)),
                ('userR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
