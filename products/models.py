from django.core.validators import MaxValueValidator
from django.db import models
from stores.models import Stores


class Products(models.Model):

    name = models.CharField(max_length=80,
                            verbose_name='Nome',
                            unique=True)

    brand = models.CharField(max_length=30,
                             verbose_name='Marca')

    ean13code = models.CharField(max_length=13,
                                 verbose_name='Código EAN-13',
                                 unique=True,
                                 blank=True,
                                 null=True)

    description = models.TextField(verbose_name='Descrição',
                                   blank=True,
                                   null=True)

    sale = models.BooleanField(verbose_name='Promoção',
                               default=False)

    featured = models.BooleanField(verbose_name='Exibir como destaque',
                                   default=False)

    full_price = models.DecimalField(verbose_name='Preço Cheio',
                                     max_digits=8,
                                     decimal_places=2)

    discount = models.PositiveSmallIntegerField(verbose_name='Desconto',
                                                default=0,
                                                validators=[
                                                    MaxValueValidator(
                                                        limit_value=100)
                                                ])

    discount_price = models.DecimalField(verbose_name='Preço com Desconto',
                                         max_digits=8,
                                         decimal_places=2)

    owner_store = models.ForeignKey(Stores,
                                    on_delete=models.CASCADE,
                                    verbose_name='Loja Detentora')

    discontinued = models.BooleanField(verbose_name='Descontinuado',
                                       default=False)

    recorded = models.DateTimeField(verbose_name='Gravado em',
                                    auto_now_add=True)

    updated = models.DateTimeField(verbose_name='Atualizado em',
                                   auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name


class ProductImages(models.Model):

    class TypeImageChoices(models.TextChoices):
        COVER = 'Capa', 'Capa'
        ADDITIONAL = 'Adicional', 'Adicional'

    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE,
                                verbose_name='Produto')

    image = models.ImageField(verbose_name='Imagem',
                              upload_to='products_images/')

    type = models.CharField(verbose_name='Tipo',
                            max_length=9,
                            choices=TypeImageChoices.choices)

    class Meta:
        ordering = ['product']
        verbose_name = 'Imagem de Produto'
        verbose_name_plural = 'Imagens de Produto'

        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['product', 'type'], name='unique_cover_image_product'
        #     )
        # ]

    def __str__(self):
        return str(self.product)
