# Generated by Django 3.2.9 on 2022-06-10 04:59

from django.db import migrations, models
import utils.rename


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20220610_1058'),
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
            field=models.CharField(default='pbkdf2_sha256$260000$eRNhLvgzVpOeb4F7SS3TUJ$Af8tVUzvWn+04nH5NAkYxdL20V3iN8ZIyooLfstXzew=', max_length=128, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=utils.rename.Rename.rename, verbose_name='Изображение'),
        ),
    ]