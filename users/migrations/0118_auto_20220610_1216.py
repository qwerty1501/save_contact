# Generated by Django 3.2.9 on 2022-06-10 06:16

from django.db import migrations, models
import utils.rename


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0117_auto_20220610_1215'),
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
            field=models.CharField(default='pbkdf2_sha256$260000$wUZC5RTYJGFlmpV0wnoJBi$EklCi/E/YtdLCCZYuPzUfYRKWXIUVSbDwk+SOPFhQ8I=', max_length=128, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=utils.rename.Rename.rename, verbose_name='Изображение'),
        ),
    ]