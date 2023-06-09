# Generated by Django 4.2.1 on 2023-06-08 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work_pictures', '0004_rename_icom_format_iconformat'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureSaveVariations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='img')),
                ('icon_75', models.ImageField(upload_to='img')),
                ('icon_50', models.ImageField(upload_to='img')),
                ('icon_25', models.ImageField(upload_to='img')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
        migrations.DeleteModel(
            name='IconFormat',
        ),
    ]
