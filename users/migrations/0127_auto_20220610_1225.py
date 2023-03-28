# Generated by Django 3.2.9 on 2022-06-10 06:25

from django.db import migrations, models
import utils.rename


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0126_auto_20220610_1224'),
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
            field=models.CharField(default='pbkdf2_sha256$260000$OItpYJZ2Eyghl6pI6RoBt8$OPPOPZeruHCcl76/J1dhd8rn8HVnlnicihEPpmjhT3c=', max_length=128, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=utils.rename.Rename.rename, verbose_name='Изображение'),
        ),
    ]