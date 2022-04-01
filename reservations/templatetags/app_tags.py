from django import template

register = template.Library()
@register.filter
def percentage(value1=2, value2=14):
    return int(value1) / int(value2) *100
