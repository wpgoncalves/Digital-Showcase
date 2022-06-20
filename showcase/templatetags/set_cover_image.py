from django import template

register = template.Library()


def set_cover_image(content, image_type):
    img = content.filter(type=image_type).first()
    return img.image.url if img is not None else None


register.filter('set_cover_image', set_cover_image)
