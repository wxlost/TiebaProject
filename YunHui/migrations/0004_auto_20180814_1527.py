# Generated by Django 2.0.7 on 2018-08-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YunHui', '0003_sign_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='success',
        ),
        migrations.AddField(
            model_name='sign',
            name='update_today',
            field=models.BooleanField(default=False, verbose_name='已更新'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='name',
            field=models.CharField(max_length=100, verbose_name='贴吧名'),
        ),
    ]
