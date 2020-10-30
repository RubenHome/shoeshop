# Generated by Django 3.1.2 on 2020-10-29 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyshoes', '0002_shoe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=4, default=0, max_digits=8)),
                ('notified', models.IntegerField(default=0)),
                ('buy_date', models.DateTimeField(auto_now=True)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyshoes.shoe')),
            ],
        ),
        migrations.CreateModel(
            name='shoesInPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('purchase', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='buyshoes.purchase')),
                ('shoe', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='buyshoes.shoe')),
            ],
        ),
    ]
