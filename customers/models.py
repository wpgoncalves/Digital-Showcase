from django.db import models
from global_models.models import Adresses, Emails, Phones


class Customers(models.Model):

    class KindChoices(models.TextChoices):
        FISICA = 'Física', 'Física'
        JURIDICA = 'Jurídica', 'Jurídica'

    name = models.CharField(verbose_name='Nome',
                            max_length=80)

    last_name = models.CharField(verbose_name='Sobrenome',
                                 max_length=20)

    kind = models.CharField(max_length=8,
                            verbose_name='Tipo',
                            choices=KindChoices.choices,
                            default='Física')

    cpf_cnpj = models.CharField(max_length=14,
                                verbose_name='CPF/CNPJ',
                                primary_key=True,
                                unique=True)

    ie_rg = models.CharField(verbose_name='IE/RG',
                             max_length=12,
                             blank=True,
                             null=True)

    country = models.CharField(verbose_name='País',
                               max_length=60,
                               blank=True,
                               null=True)

    passport = models.CharField(verbose_name='Passaporte',
                                max_length=8,
                                blank=True,
                                null=True)

    responsible = models.CharField(verbose_name='Responsável',
                                   max_length=100,
                                   blank=True,
                                   null=True)

    address = models.ManyToManyField(Adresses,
                                     verbose_name='Endereço',
                                     blank=True)

    address_number = models.IntegerField(verbose_name='Número',
                                         blank=True,
                                         null=True)

    address_complement = models.CharField(verbose_name='Complemento',
                                          max_length=120,
                                          blank=True,
                                          null=True)

    phones = models.ManyToManyField(Phones,
                                    verbose_name='Telefones',
                                    blank=True)

    emails = models.ManyToManyField(Emails,
                                    verbose_name='E-mails',
                                    blank=True)

    recorded = models.DateTimeField(verbose_name='Gravado em',
                                    auto_now_add=True)

    updated = models.DateTimeField(verbose_name='Atualizado em',
                                   auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name
