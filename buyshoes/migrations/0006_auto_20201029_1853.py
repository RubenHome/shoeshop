# Generated by Django 3.1.2 on 2020-10-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyshoes', '0005_auto_20201029_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
