# Generated by Django 2.2.5 on 2020-01-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementsystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendemp',
            name='catagory',
            field=models.CharField(choices=[('ADID', 'ADID'), ('UNADID', 'UNADID'), ('STUFF', 'STUFF')], default='ADID', max_length=15),
        ),
        migrations.AddField(
            model_name='extendemp',
            name='department',
            field=models.CharField(choices=[('ARTS', 'ARTS'), ('SCIENCE', 'SCIENCE'), ('COMMERCE', 'COMMERCE')], default='ARTS', max_length=15),
        ),
    ]