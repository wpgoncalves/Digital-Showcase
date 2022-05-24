from django.contrib import admin

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    form = NewsletterForm
    list_display = ('name', 'email', 'signed')
    search_fields = ('name', 'email')
    fieldsets = (
        (None, {
            'fields': ('name', 'email'),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )
