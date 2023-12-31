# Generated by Django 4.2.6 on 2023-11-01 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_imag/')),
                ('alt', models.CharField(blank=True, max_length=25)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productdetails')),
            ],
        ),
    ]
