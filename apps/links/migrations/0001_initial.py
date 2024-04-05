# Generated by Django 5.0.3 on 2024-03-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastroLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('publicada', models.BooleanField(default=False)),
            ],
        ),
    ]