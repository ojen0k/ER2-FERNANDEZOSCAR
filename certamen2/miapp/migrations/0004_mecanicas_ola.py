# Generated by Django 4.2.6 on 2023-10-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_informaticas_mecanicas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecanicas',
            name='ola',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]