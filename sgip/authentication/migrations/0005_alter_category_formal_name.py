# Generated by Django 5.0.4 on 2024-04-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_category_formal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='formal_name',
            field=models.CharField(max_length=100),
        ),
    ]