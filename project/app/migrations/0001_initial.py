# Generated by Django 4.0.5 on 2022-06-03 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtype', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date', models.DateField()),
                ('description', models.TextField(null=True)),
                ('dtype', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.dtype')),
            ],
        ),
    ]
