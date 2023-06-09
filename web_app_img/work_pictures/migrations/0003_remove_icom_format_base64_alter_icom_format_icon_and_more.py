# Generated by Django 4.1.3 on 2023-06-03 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work_pictures', '0002_rename_icom_format_st_icom_format'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icom_format',
            name='base64',
        ),
        migrations.AlterField(
            model_name='icom_format',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='work_pictures/static/img'),
        ),
        migrations.AlterField(
            model_name='icom_format',
            name='icon_25',
            field=models.ImageField(blank=True, null=True, upload_to='work_pictures/static/img'),
        ),
        migrations.AlterField(
            model_name='icom_format',
            name='icon_50',
            field=models.ImageField(blank=True, null=True, upload_to='work_pictures/static/img'),
        ),
        migrations.AlterField(
            model_name='icom_format',
            name='icon_75',
            field=models.ImageField(blank=True, null=True, upload_to='work_pictures/static/img'),
        ),
        migrations.AlterField(
            model_name='icom_format',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач'),
        ),
    ]
