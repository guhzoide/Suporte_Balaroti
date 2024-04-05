# Generated by Django 5.0.3 on 2024-03-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0007_alter_cadastrolojas_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadastroCameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(max_length=10)),
                ('loja', models.CharField(max_length=5)),
                ('ip', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='cadastrolojas',
            name='cnpj',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='cadastrolojas',
            name='regiao',
            field=models.CharField(max_length=3),
        ),
    ]