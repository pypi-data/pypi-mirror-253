from django import template
from django.utils.html import format_html_join

from django_cotton.templatetags._component import cotton_component
from django_cotton.templatetags._slot import cotton_slot
from django_cotton.templatetags._attrs import cotton_attrs
from django_cotton.templatetags._var import cotton_var

register = template.Library()

register.tag("cotton_component", cotton_component)
register.tag("cotton_slot", cotton_slot)
register.filter("cotton_attrs", cotton_attrs)
register.tag("cotton_var", cotton_var)


# @register.filter
# def attr_merge(value, arg):
#     # value is expected to be a dictionary of attributes from the context
#     # arg is a string representing the default attributes, e.g., "class:border-t"
#     default_attr_key, default_attr_value = arg.split(':')
#     merged_value = value.get(default_attr_key, '') + ' ' + default_attr_value
#     return format_html_join(' ', "{0}='{1}'", [(default_attr_key, merged_value.strip())])