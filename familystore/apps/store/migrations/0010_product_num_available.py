# Generated by Django 3.1.2 on 2020-10-30 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num_available',
            field=models.IntegerField(default=1),
        ),
    ]