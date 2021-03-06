# Generated by Django 4.0.2 on 2022-02-08 02:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Workday',
            fields=[
                ('fileno', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=10)),
                ('work_date', models.DateField(default=datetime.date.today)),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('hours_code', models.CharField(max_length=10)),
                ('FBP_payroll', models.FloatField()),
                ('AMCO_payroll', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workdaymanagement.location')),
            ],
        ),
    ]
