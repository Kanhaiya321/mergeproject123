# Generated by Django 3.2.12 on 2022-11-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_user_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobileNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
