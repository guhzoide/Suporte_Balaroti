# Generated by Django 5.0.3 on 2024-03-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0008_cadastrocameras_alter_cadastrolojas_cnpj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrocameras',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]