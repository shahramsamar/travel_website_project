# Generated by Django 4.2.7 on 2024-02-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='blog/'),
            preserve_default=False,
        ),
    ]
