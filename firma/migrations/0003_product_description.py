# Generated by Django 5.0.4 on 2024-05-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firma", "0002_customuser_email_confirmed"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.CharField(default="Opis", max_length=200),
        ),
    ]
