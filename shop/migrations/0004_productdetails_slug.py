# Generated by Django 4.2.6 on 2023-11-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_img_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]