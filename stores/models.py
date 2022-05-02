from django.db import models
from django.urls import reverse


class Stores(models.Model):

    cnpj = models.CharField(verbose_name='CNPJ',
                            max_length=14,
                            primary_key=True,
                            unique=True)

    business_name = models.CharField(verbose_name='Razão Social',
                                     max_length=100)

    title_establishment = models.CharField(verbose_name='Fantasia',
                                           max_length=50)

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

    def get_absolute_url(self):
        return reverse("chosen-store", kwargs={"slug": self.slug})
