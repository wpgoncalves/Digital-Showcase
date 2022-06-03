from customers.models import Adresses, Emails, Phones
from django.core.exceptions import ValidationError
from django.db import models
from validate_docbr import CNPJ


class Stores(models.Model):

    class GroupChoices(models.TextChoices):
        CANDY = 'Doceria', 'Doceria'
        SNACK_BAR = 'Lanchonete', 'Lanchonete'
        PIZZERIA = 'Pizzaria', 'Pizzaria'
        RESTAURANT = 'Restaurante', 'Restaurante'
        CLOTHING = 'Vestuário', 'Vestuário'

    def validate_cnpj(value):
        if not CNPJ().validate(value):
            raise ValidationError('CNPJ inválido.')

    cnpj = models.CharField(verbose_name='CNPJ',
                            max_length=14,
                            validators=[validate_cnpj],
                            primary_key=True,
                            unique=True)

    business_name = models.CharField(verbose_name='Razão Social',
                                     max_length=100)

    title_establishment = models.CharField(verbose_name='Fantasia',
                                           max_length=27,
                                           unique=True)

    group = models.CharField(verbose_name='Grupo',
                             choices=GroupChoices.choices,
                             max_length=15)

    address = models.OneToOneField(Adresses,
                                   verbose_name='Endereço',
                                   on_delete=models.PROTECT,
                                   blank=True,
                                   null=True)

    address_number = models.PositiveIntegerField(verbose_name='Número',
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

    slug = models.SlugField(verbose_name='Slug',
                            max_length=50,
                            unique=True)

    active = models.BooleanField(verbose_name='Ativa',
                                 default=True)

    class Meta:
        ordering = ['business_name']
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'

    def __str__(self):
        return self.business_name


class SocialNetworks(models.Model):

    class MediaChoices(models.TextChoices):
        FACEBOOK = 'Facebook', 'Facebook'
        INSTAGRAM = 'Instagram', 'Instagram'
        TWITTER = 'Twitter', 'Twitter'
        WHATSAPP = 'Whatsapp', 'Whatsapp'
        YOUTUBE = 'Youtube', 'Youtube'

    store_holder = models.ForeignKey(Stores,
                                     on_delete=models.CASCADE,
                                     verbose_name='Loja Detentora')

    media = models.CharField(verbose_name='Rede Social',
                             choices=MediaChoices.choices,
                             max_length=10)

    url = models.URLField(verbose_name='URL',
                          unique=True)

    class Meta:
        ordering = ['store_holder']
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

    def __str__(self):
        return self.url
