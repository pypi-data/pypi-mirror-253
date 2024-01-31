from django import template
from django.utils.safestring import mark_safe

# register = template.Library()


# @register.filter
def cotton_attrs(attrs):
    return mark_safe('test="hellp"')
    print(attrs, 'ATTRS')
    attrs = attrs.replace('=""', '')
    test = mark_safe(attrs)

    return test
