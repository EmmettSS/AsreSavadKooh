# Generated by Django 5.0 on 2024-07-23 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0006_alter_address_post_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='شهر یا منطقه'),
        ),
    ]
