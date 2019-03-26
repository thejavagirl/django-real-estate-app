# Generated by Django 2.1.7 on 2019-03-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(),
        ),
    ]
