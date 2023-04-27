# Generated by Django 4.1.6 on 2023-04-24 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_purchase_rename_limited_product_is_limited_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фото товара', 'verbose_name_plural': 'Фото товаров'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='promocode',
            options={'verbose_name': 'Промокод на скидку', 'verbose_name_plural': 'Промокоды на скидку'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Запрос на покупку', 'verbose_name_plural': 'Запросы на покупки'},
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(help_text='Будет выводиться на главной странице. Максимум - 300 символов.', max_length=300, null=True, verbose_name='Краткое описание'),
        ),
    ]