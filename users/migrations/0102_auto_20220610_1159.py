# Generated by Django 3.2.9 on 2022-06-10 05:59

from django.db import migrations, models
import utils.rename


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0101_auto_20220610_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=utils.rename.Rename.rename, verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bg',
            field=models.ImageField(blank=True, null=True, upload_to=utils.rename.Rename.rename, verbose_name='Задний фон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$9AWo8rJadIaXwpGdiH2CSf$zrvnAg29THj0OC4gga7BtagSD94qqvgSPKdZAs9+u+U=', max_length=128, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=utils.rename.Rename.rename, verbose_name='Изображение'),
        ),
    ]