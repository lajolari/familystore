# Generated by Django 3.1.2 on 2020-10-30 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_productimage'),
        ('order', '0005_auto_20201029_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped'), ('arrived', 'Arrived')], default='ordered', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='store.product'),
        ),
    ]