# Generated by Django 5.1.1 on 2024-09-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_borrowrecord_student_delete_s'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('student_id', models.IntegerField()),
            ],
            options={
                'db_table': 'library_s',
            },
        ),
    ]
