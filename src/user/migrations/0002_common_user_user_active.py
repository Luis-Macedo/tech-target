# Generated by Django 4.0.4 on 2022-05-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='common_user',
            name='user_active',
            field=models.BooleanField(default=True),
        ),
    ]
