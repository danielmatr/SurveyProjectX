# Generated by Django 3.2.7 on 2022-04-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_infouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/user_image'),
        ),
    ]
