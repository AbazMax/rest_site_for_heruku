# Generated by Django 4.1.1 on 2022-09-15 18:40

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_gallery_is_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefs',
            name='photo',
            field=models.ImageField(default=1, upload_to=main.models.Chefs.get_file_name),
            preserve_default=False,
        ),
    ]
