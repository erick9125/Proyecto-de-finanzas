# Generated by Django 2.1.2 on 2018-11-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('apellido', models.CharField(max_length=50)),
                ('clave', models.CharField(blank=True, max_length=30, null=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
