# Generated by Django 5.0.3 on 2024-03-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0009_cadastrocameras_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrocameras',
            name='ip',
            field=models.CharField(max_length=10),
        ),
    ]
