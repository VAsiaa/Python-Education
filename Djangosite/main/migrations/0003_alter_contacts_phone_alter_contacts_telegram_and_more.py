# Generated by Django 5.0.4 on 2024-05-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_contacts_phone_alter_contacts_telegram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='telegram',
            field=models.TextField(blank=True, null=True, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='education',
            name='eduDepartment',
            field=models.TextField(blank=True, null=True, verbose_name='Факультет'),
        ),
        migrations.AlterField(
            model_name='education',
            name='eduQualification',
            field=models.TextField(blank=True, null=True, verbose_name='Квалификация'),
        ),
    ]
