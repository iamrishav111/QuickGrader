# Generated by Django 3.1.4 on 2020-12-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign_db', '0002_auto_20201209_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='file_name',
        ),
        migrations.AddField(
            model_name='destination',
            name='doc',
            field=models.FileField(default=0, upload_to='assignments'),
            preserve_default=False,
        ),
    ]
