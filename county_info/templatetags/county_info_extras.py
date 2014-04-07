from django import template

register = template.Library()

# Custom Template Filters & tags
@register.filter(name='multiply')
def multiply(value, arg):
	if value != None:
		return value*arg