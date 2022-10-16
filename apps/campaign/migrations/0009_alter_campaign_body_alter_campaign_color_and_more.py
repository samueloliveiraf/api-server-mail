# Generated by Django 4.0.8 on 2022-10-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0008_alter_campaign_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='body',
            field=models.TextField(default=1, verbose_name='Mensagem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='color',
            field=models.CharField(default=1, max_length=5000, verbose_name='Informe a cor. A cor só podem ser = azul ou verde ou vermelho, informe em texto e tudo minusculo sem espaço'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='email_from',
            field=models.CharField(default=2, max_length=5000, verbose_name='Email de envio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=models.CharField(max_length=5000, verbose_name='Link da imagem'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='subject',
            field=models.CharField(max_length=5000, verbose_name='Cabeçalho'),
        ),
    ]