# Generated by Django 4.0.3 on 2022-05-01 09:01

from django.db import migrations, models
import utils.rename


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0028_alter_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to=utils.rename.Rename.rename, verbose_name='Фото'),
        ),
    ]
