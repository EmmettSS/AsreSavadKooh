# Generated by Django 5.0 on 2024-07-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_gallery_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_text', models.TextField(null=True, verbose_name='متن معرفی')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='ایمیل ارتباطی')),
                ('phone_number', models.CharField(max_length=100, null=True, verbose_name='شماره تلفن ارتباظی')),
            ],
            options={
                'verbose_name': 'صفحه درباره',
                'verbose_name_plural': 'مدیریت صفحه درباره',
            },
        ),
    ]
