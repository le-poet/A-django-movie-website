# Generated by Django 3.0.5 on 2020-05-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iflix', '0002_auto_20200430_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
