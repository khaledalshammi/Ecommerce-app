# Generated by Django 3.0.14 on 2022-07-26 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20220726_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Payment'),
        ),
    ]
