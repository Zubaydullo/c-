# Generated by Django 3.2.2 on 2021-08-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="My Freakin' Awesome Blog!", max_length=255),
        ),
    ]
