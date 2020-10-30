# Generated by Django 3.1.2 on 2020-10-30 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyshoes', '0008_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='buy_date',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='notified',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchase',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='total_amount',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='client_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.DeleteModel(
            name='shoesInPurchase',
        ),
    ]
