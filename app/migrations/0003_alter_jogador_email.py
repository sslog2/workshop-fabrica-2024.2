# Generated by Django 5.1 on 2024-08-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_personagem_pontos_de_vida_jogador_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
    ]
