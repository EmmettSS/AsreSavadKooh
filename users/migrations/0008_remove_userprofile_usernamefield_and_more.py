# Generated by Django 5.0 on 2024-07-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_delete_aboutus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='usernamefield',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email_active_code',
            field=models.CharField(max_length=100, null=True, verbose_name='کد فعالسازی ایمیل'),
        ),
    ]
