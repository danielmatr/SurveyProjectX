# Generated by Django 3.2.7 on 2022-04-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Image'),
        ),
    ]
