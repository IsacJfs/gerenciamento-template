# Generated by Django 4.2.4 on 2023-08-28 17:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0021_alter_ingredienteordemservico_qtde'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrusao',
            old_name='data',
            new_name='data_fim',
        ),
        migrations.AddField(
            model_name='extrusao',
            name='data_inicio',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extrusao',
            name='produto_ingrediente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='produto_ordem_servico', to='gerenciamento.ingredienteordemservico'),
            preserve_default=False,
        ),
    ]
