from django.db import models
from apps.accounts.models import User


class Campaign(models.Model):
    subject = models.CharField(
        max_length=5000,
        verbose_name='Cabeçalho'
    )
    image = models.CharField(
        max_length=5000,
        verbose_name='Link da imagem'
    )
    email_from = models.CharField(
        max_length=5000,
        verbose_name='Email de envio'
    )
    color = models.CharField(
        max_length=5000,
        verbose_name='Informe a cor. '
        'A cor só podem ser = azul ou verde ou vermelho, '
        'informe em texto e tudo minusculo sem espaço',
    )
    emails_destiny = models.TextField(
        verbose_name='Informe os emails de destino separado por vírgula'
    )
    body = models.TextField(
        verbose_name='Mensagem'
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'
        db_table = 'campaigns'
