# Generated by Django 5.0 on 2024-06-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='تصویر کاور'),
        ),
        migrations.AddField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='قابل مشاهده / غیرقابل مشاهده'),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url'),
        ),
        migrations.AddField(
            model_name='category',
            name='url_title',
            field=models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='عنوان در url'),
        ),
    ]