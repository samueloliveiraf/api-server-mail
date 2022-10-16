from django.db import models
from apps.accounts.models import User


class Campaign(models.Model):
    COLOR_CHOICES = [
        ('vermelho', 'vermelho'),
        ('azul', 'azul'),
        ('verde', 'verde')
    ]
    subject = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
        verbose_name='Cabeçalho'
    )
    image = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
        verbose_name='Link da imagem'
    )
    email_from = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
        verbose_name='Email de envio'
    )
    color = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
        choices=COLOR_CHOICES,
        verbose_name='Cor'
    )
    emails_destiny = models.TextField(
        verbose_name='Informe os emails de destino separado por vírgula'
    )
    body = models.TextField(
        null=True,
        blank=True,
        verbose_name='Mensagem'
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'
        db_table = 'campaigns'
