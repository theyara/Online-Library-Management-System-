# Generated by Django 5.1.1 on 2024-09-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_s_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
