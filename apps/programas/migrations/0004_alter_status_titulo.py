# Generated by Django 5.0.3 on 2024-03-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0003_status_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='titulo',
            field=models.CharField(default='', max_length=5),
        ),
    ]
