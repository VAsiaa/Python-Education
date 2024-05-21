# Generated by Django 5.0.4 on 2024-05-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_mailnotification_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailnotification',
            name='mailSmtpPort',
            field=models.IntegerField(default=465, verbose_name='SMTP порт'),
        ),
        migrations.AddField(
            model_name='mailnotification',
            name='mailSmtpServer',
            field=models.CharField(default='default smpt', max_length=255, verbose_name='SMTP сервер'),
            preserve_default=False,
        ),
    ]
