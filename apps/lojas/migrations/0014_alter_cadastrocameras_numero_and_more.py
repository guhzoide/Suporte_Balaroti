# Generated by Django 5.0.3 on 2024-03-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0013_alter_cadastrocameras_vnc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrocameras',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cadastrolojas',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
