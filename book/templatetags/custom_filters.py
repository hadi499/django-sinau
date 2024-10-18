from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def clean_whitespace(value):
    if isinstance(value, str):
        # Menghapus karakter non-breaking dan spasi
        cleaned_value = value.replace('&nbsp;', '').strip()
        # Menghapus tag HTML
        return strip_tags(cleaned_value)
    return value