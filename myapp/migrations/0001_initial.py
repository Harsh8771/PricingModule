# Generated by Django 4.2 on 2023-04-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricingConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_base_price', models.IntegerField(default=0)),
                ('distance_additional_price', models.IntegerField(default=1)),
                ('time_multiplier_factor', models.IntegerField(default=1)),
                ('enable', models.BooleanField(default=False)),
                ('distance_limit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('time_limit', models.DurationField(default=0)),
            ],
        ),
    ]
