# Generated by Django 4.0.2 on 2022-03-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextended',
            name='username',
            field=models.EmailField(default=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
