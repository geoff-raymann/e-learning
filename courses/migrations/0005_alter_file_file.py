# Generated by Django 4.2 on 2023-05-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=200, upload_to=''),
        ),
    ]
