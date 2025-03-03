# Generated by Django 4.0.2 on 2022-04-09 01:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_like_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='store_avatars/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='restaurants.restaurant')),
            ],
        ),
    ]
