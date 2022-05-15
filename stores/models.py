from django.core.exceptions import ValidationError
from django.db import models
# from django.urls import reverse
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

    # def get_absolute_url(self):
    #     return reverse("chosen-store", kwargs={"slug": self.slug})
