# Generated by Django 5.0 on 2024-07-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0004_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.DecimalField(decimal_places=1, max_digits=50, null=True, verbose_name='کد پستی یا شماره تلفن'),
        ),
    ]
