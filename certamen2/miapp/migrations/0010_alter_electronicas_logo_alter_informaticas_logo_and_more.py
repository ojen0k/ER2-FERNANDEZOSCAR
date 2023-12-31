# Generated by Django 4.2.6 on 2023-10-24 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('miapp', '0009_electronicas_logo_informaticas_logo_mecanicas_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicas',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='miapp/static/miapp/img/'),
        ),
        migrations.AlterField(
            model_name='informaticas',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='miapp/static/miapp/img/'),
        ),
        migrations.AlterField(
            model_name='mecanicas',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='miapp/static/miapp/img/'),
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]
