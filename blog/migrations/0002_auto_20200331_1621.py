# Generated by Django 3.0.3 on 2020-03-31 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
