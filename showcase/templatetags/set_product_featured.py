from django import template

register = template.Library()


def set_product_featured(content, featured=True):
    return content.filter(featured=featured)


register.filter('set_product_featured', set_product_featured)
