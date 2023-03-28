# Generated by Django 3.2.9 on 2022-06-10 05:14

from django.db import migrations, models
import utils.rename


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0085_alter_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to=utils.rename.Rename.rename, verbose_name='Фото'),
        ),
    ]
