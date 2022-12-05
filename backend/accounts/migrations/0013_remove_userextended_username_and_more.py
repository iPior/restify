# Generated by Django 4.0.2 on 2022-03-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_userextended_username_alter_userextended_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextended',
            name='username',
        ),
        migrations.AlterField(
            model_name='userextended',
            name='email',
            field=models.EmailField(default=True, max_length=254, unique=True),
        ),
    ]
