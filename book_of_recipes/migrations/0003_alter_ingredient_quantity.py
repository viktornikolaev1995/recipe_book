# Generated by Django 3.2.9 on 2022-02-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_of_recipes', '0002_alter_ingredient_unit_of_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.CharField(max_length=50, verbose_name='Количество'),
        ),
    ]
