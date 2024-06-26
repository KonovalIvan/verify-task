# Generated by Django 5.0.6 on 2024-05-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("-", "No category"),
                    ("F", "Food"),
                    ("C", "Consumables"),
                    ("M", "Manufactured"),
                    ("S", "Services"),
                ],
                default="-",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, default="", max_length=2000),
        ),
    ]
