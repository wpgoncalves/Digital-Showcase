from django.db import models


class SocialNetworks(models.Model):

    class MediaChoices(models.TextChoices):
        FACEBOOK = 'Facebook', 'Facebook'
        INSTAGRAM = 'Instagram', 'Instagram'
        TWITTER = 'Twitter', 'Twitter'
        WHATSAPP = 'Whatsapp', 'Whatsapp'
        YOUTUBE = 'Youtube', 'Youtube'

    url = models.URLField(verbose_name='URL',
                          primary_key=True,
                          unique=True)

    media = models.CharField(verbose_name='Rede Social',
                             choices=MediaChoices.choices,
                             max_length=10)

    class Meta:
        ordering = ['url']
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

    def __str__(self):
        return self.url
