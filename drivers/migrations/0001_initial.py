# Generated by Django 5.0.1 on 2024-01-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('minimum', models.PositiveIntegerField()),
                ('sum_per_km', models.PositiveIntegerField()),
                ('waiting_cost', models.PositiveIntegerField()),
                ('baggage_cost', models.PositiveIntegerField()),
                ('bonus_percent', models.PositiveSmallIntegerField()),
                ('firm_percent', models.PositiveIntegerField()),
            ],
        ),
    ]
