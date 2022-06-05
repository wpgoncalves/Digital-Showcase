from django.db import models


class Adresses(models.Model):

    class StateChoices(models.TextChoices):
        RONDONIA = 'RO', 'Rondônia'
        ACRE = 'AC', 'Acre'
        AMAZONAS = 'AM', 'Amazonas'
        RORAIMA = 'RR', 'Roraima'
        PARA = 'PA', 'Pará'
        AMAPA = 'AP', 'Amapá'
        TOCANTIS = 'TO', 'Tocantins'
        MARANHAO = 'MA', 'Maranhão'
        PIAUI = 'PI', 'Piauí'
        CEARA = 'CE', 'Ceará'
        RIO_GRANDE_DO_NORTE = 'RN', 'Rio Grande do Norte'
        PARAIBA = 'PB', 'Paraíba'
        PERNAMBUCO = 'PE', 'Pernambuco'
        ALAGOAS = 'AL', 'Alagoas'
        SERGIPE = 'SE', 'Sergipe'
        BAHIA = 'BA', 'Bahia'
        MINAS_GERAIS = 'MG', 'Minas Gerais'
        ESPIRITO_SANTO = 'ES', 'Espírito Santo'
        RIO_DE_JANEIRO = 'RJ', 'Rio de Janeiro'
        SAO_PAULO = 'SP', 'São Paulo'
        PARANA = 'PR', 'Paraná'
        SANTA_CATARINA = 'SC', 'Santa Catarina'
        RIO_GRANDE_DO_SULA = 'RS', 'Rio Grande do Sul'
        MATO_GROSSO_DO_SUL = 'MS', 'Mato Grosso do Sul'
        MATO_GROSSO = 'MT', 'Mato Grosso'
        GOIAS = 'GO', 'Goiás'
        DISTRITO_FEDERAL = 'DF', 'Distrito Federal'

    class TypeChoices(models.TextChoices):
        AEROPORTO = 'Aeroporto', 'Aeroporto'
        ALAMEDA = 'Alameda', 'Alameda'
        AREA = 'Área', 'Área'
        AVENIDA = 'Avenida', 'Avenida'
        CAMPO = 'Campo', 'Campo'
        CHACARA = 'Chácara', 'Chácara'
        COLONIA = 'Colônia', 'Colônia'
        CONDOMINIO = 'Condomínio', 'Condomínio'
        CONJUNTO = 'Conjunto', 'Conjunto'
        DISTRITO = 'Distrito', 'Distrito'
        ESPLANADA = 'Esplanada', 'Esplanada'
        ESTACAO = 'Estação', 'Estação'
        ESTRADA = 'Estrada', 'Estrada'
        FAVELA = 'Favela', 'Favela'
        FAZENDA = 'Fazenda', 'Fazenda'
        FEIRA = 'Feira', 'Feira'
        JARDIM = 'Jardim', 'Jardim'
        LADEIRA = 'Ladeira', 'Ladeira'
        LAGO = 'Lago', 'Lago'
        LAGOA = 'Lagoa', 'Lagoa'
        LARGO = 'Largo', 'Largo'
        LOTEAMENTO = 'Loteamento', 'Loteamento'
        MORRO = 'Morro', 'Morro'
        NUCLEO = 'Núcleo', 'Núcleo'
        PARQUE = 'Parque', 'Parque'
        PASSARELA = 'Passarela', 'Passarela'
        PATIO = 'Pátio', 'Pátio'
        PRACA = 'Praça', 'Praça'
        QUADRA = 'Quadra', 'Quadra'
        RECANTO = 'Recanto', 'Recanto'
        RESIDENCIAL = 'Residencial', 'Residencial'
        RODOVIA = 'Rodovia', 'Rodovia'
        RUA = 'Rua', 'Rua'
        SETOR = 'Setor', 'Setor'
        SITIO = 'Sítio', 'Sítio'
        TRAVESSA = 'Travessa', 'Travessa'
        TRECHO = 'Trecho', 'Trecho'
        TREVO = 'Trevo', 'Trevo'
        VALE = 'Vale', 'Vale'
        VEREDA = 'Vereda', 'Vereda'
        VIA = 'Via', 'Via'
        VIADUTO = 'Viaduto', 'Viaduto'
        VIELA = 'Viela', 'Viela'
        VILA = 'Vila', 'Vila'

    cep = models.CharField(max_length=8,
                           verbose_name='CEP',
                           primary_key=True,
                           unique=True)

    type = models.CharField(max_length=60,
                            verbose_name='Tipo',
                            choices=TypeChoices.choices)

    address = models.CharField(max_length=255,
                               verbose_name='Endereço')

    district = models.CharField(max_length=120,
                                verbose_name='Bairro')

    city = models.CharField(max_length=120,
                            verbose_name='Cidade')

    state = models.CharField(max_length=2,
                             verbose_name='UF',
                             choices=StateChoices.choices)

    class Meta:
        ordering = ['cep']
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.type + ' ' + self.address


class Phones(models.Model):

    class TypeChoices(models.TextChoices):
        HOME = 'Residêncial', 'Residêncial'
        CELL = 'Celular', 'Celular'
        COMMERCIAL = 'Comercial', 'Comercial'

    number = models.CharField(max_length=11,
                              verbose_name='Telefone',
                              primary_key=True,
                              unique=True)

    type = models.CharField(max_length=11,
                            verbose_name='Tipo',
                            choices=TypeChoices.choices)

    comments = models.TextField(verbose_name='Observações',
                                blank=True,
                                null=True)

    class Meta:
        ordering = ['number']
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return self.number


class Emails(models.Model):

    email = models.EmailField(verbose_name='E-mail',
                              primary_key=True,
                              unique=True)

    class Meta:
        ordering = ['email']
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email


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
