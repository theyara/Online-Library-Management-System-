# Generated by Django 5.1.1 on 2024-09-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_librarys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarys',
            name='student_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='librarys',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
