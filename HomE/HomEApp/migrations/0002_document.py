# Generated by Django 4.1.7 on 2023-03-12 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomEApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.TextField(max_length=30)),
                ('document_upload', models.FileField(upload_to='media')),
                ('document_tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomEApp.tenent')),
            ],
        ),
    ]