from django import template

register = template.Library()


def set_product(content, product):
    return content.filter(product=product)


register.filter('set_product', set_product)
