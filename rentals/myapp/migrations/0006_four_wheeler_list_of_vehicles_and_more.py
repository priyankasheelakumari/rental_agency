# Generated by Django 4.2.3 on 2023-07-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_two_wheeler_userr1'),
    ]

    operations = [
        migrations.AddField(
            model_name='four_wheeler',
            name='List_of_vehicles',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='two_wheeler',
            name='List_of_vehicles',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
