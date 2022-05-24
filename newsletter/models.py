from django.db import models


class Newsletter(models.Model):

    name = models.CharField(verbose_name='Nome completo',
                            max_length=100)

    email = models.EmailField(verbose_name='E-mail',
                              primary_key=True,
                              unique=True)

    signed = models.DateTimeField(verbose_name='Assinado em',
                                  auto_now=True,
                                  editable=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Boletim Informativo'
        verbose_name_plural = 'Boletins Informativos'

    def __str__(self):
        return self.email
