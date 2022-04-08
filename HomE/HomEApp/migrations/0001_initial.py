# Generated by Django 4.0.3 on 2022-04-08 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_name', models.CharField(max_length=100)),
                ('home_location', models.CharField(max_length=255)),
                ('home_address', models.CharField(max_length=255)),
                ('home_rent', models.IntegerField()),
                ('home_floor', models.CharField(max_length=20)),
                ('home_painting_money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenent_name', models.CharField(max_length=200)),
                ('tenent_start_date', models.DateTimeField()),
                ('tenent_end_date', models.DateTimeField()),
                ('tenent_advance', models.IntegerField()),
                ('tenent_note', models.TextField(max_length=500)),
                ('tenent_home_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomEApp.home')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_month', models.IntegerField()),
                ('rent_year', models.IntegerField()),
                ('rent_recived_date', models.DateTimeField()),
                ('rent_amount', models.IntegerField()),
                ('rent_tenent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomEApp.tenent')),
            ],
        ),
    ]
