# Generated by Django 5.0.3 on 2024-03-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0015_remove_cadastrocameras_vnc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrocameras',
            name='ip',
            field=models.CharField(max_length=20),
        ),
    ]
