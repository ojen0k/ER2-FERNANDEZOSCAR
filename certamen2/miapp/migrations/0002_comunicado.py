# Generated by Django 4.2.6 on 2023-10-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('detalle', models.CharField(max_length=250)),
                ('detalle_corto', models.CharField(max_length=50)),
            ],
        ),
    ]
