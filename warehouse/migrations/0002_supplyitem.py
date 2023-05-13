# Generated by Django 4.2.1 on 2023-05-11 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_product_amount'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='Кол-во товара')),
                ('product', models.ForeignKey(help_text='Выберите или создайте товар, который присутствует в данной поствке, и добавьте его кол-во.', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pages.product', verbose_name='Товар')),
            ],
        ),
    ]
